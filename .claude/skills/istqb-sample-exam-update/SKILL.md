---
name: istqb-sample-exam-update
description: Brings an ISTQB CTFL Polish sample-exam set (sample-exam-pl/sample-exam-pl-<letter>/questions-<letter>-pl.md in this repo) up to date from a newly downloaded pair of official PQB/ISTQB PDFs -- a "pytania" (questions) PDF and an "odpowiedzi" (answers) PDF for one set letter (A, B, C, D, ...). Use this skill whenever the user attaches or references a zestaw-<letter>-pytania and zestaw-<letter>-odpowiedzi PDF pair (any version) and asks to update, complete, sync, or "do the same for set X" as a previous set -- even if they don't spell out the steps, since this is a fixed multi-stage extraction-and-transcription workflow that's easy to get subtly wrong by hand (missed bold emphasis, misread diagrams, off-by-one separator bugs when appending). Also use it when the user asks to check an existing set's file against a newer PDF version for corrections/errata, or to fill in a partially-transcribed set (e.g. only the first few questions exist and the rest need completing).
---

# ISTQB sample-exam set update

## What this actually is

Each ISTQB sample-exam set PDF pair (pytania + odpowiedzi) contains 40 main
questions and sometimes a 26-question appendix ("Dodatek A"). The repo's
`questions-<letter>-pl.md` files are hand-authored transcriptions of these
into a specific markdown schema that the upstream `istqborg/istqb_product_base`
LaTeX+pandoc pipeline consumes at build time. `questions.yml` in the same
directory is a **gitignored, regenerated build artifact** -- never treat it
as a source, never edit it, delete any stray copy before finishing (it's
harmless but confusing to leave lying around, and it'll never appear in
`git status` since it's ignored).

Your job is not "summarize the PDF" -- it's "produce a byte-faithful
transcription that a strict downstream parser will accept, with every
bold/italic emphasis, table, diagram, and formula preserved as it actually
appears in the source, appended cleanly onto whatever's already there."
That precision is why this is a skill and not just "read the PDF and write
markdown": eyeballing a 40-question PDF and writing prose from memory
reliably drops emphasis markers, mis-transcribes tables, and gets separator
bytes wrong at the append point. Every step below exists because it's where
that kind of error actually happened before.

## Step 1 -- Inventory what's already there

Read the target `questions-<letter>-pl.md` in full before touching
anything. Note the number of questions already present and their learning
objectives (`lo:` field). Don't assume the file is complete just because it
exists -- it's common for only the first handful of questions to have been
transcribed from an older PDF version, with the rest still missing. Compare
the existing `lo:` values against the new PDF's table of contents to see
exactly which questions (if any) already exist and which are new.

Also check `metadata.yml` in the same directory -- its `version` field
tells you which PDF revision the existing content was transcribed from,
which matters for step 7 (an old `version: v1.3` next to a PDF marked
"wersja 1.7" is a strong signal that even the "already transcribed"
questions might have received corrections since and are worth
double-checking, not just trusting).

## Step 2 -- Extract PDF text *with* formatting, not just text

Plain `page.extract_text()` throws away bold/italic emphasis, and ISTQB
questions lean on that emphasis to change the meaning of the question
("która **najlepiej**..." vs "która..."). Use `pdfplumber` and reconstruct
emphasis from font metadata instead of guessing which words sound
emphasis-worthy:

```python
import pdfplumber

def extract_bold_marked(pdf_path):
    out = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words(extra_attrs=["fontname"], use_text_flow=False)
            lines = {}
            for w in words:
                lines.setdefault(round(w["top"], 1), []).append(w)
            for top in sorted(lines):
                parts = []
                for w in sorted(lines[top], key=lambda w: w["x0"]):
                    txt = w["text"]
                    if "Bold" in w["fontname"]:
                        txt = f"**{txt}**"
                    if "Italic" in w["fontname"] or "Oblique" in w["fontname"]:
                        txt = f"_{txt}_"  # just a marker for you to read; final prose uses *single* asterisks, see references/markdown-conventions.md
                    parts.append(txt)
                out.append(" ".join(parts))
            out.append(f"===PAGE {page.page_number}===")
    return "\n".join(out)
```

Run this for *both* PDFs (questions and answers) and save the output to a
scratch file you can grep and re-read -- you'll be going back to it
repeatedly. If `pdfplumber` isn't installed, `python3 -m pip install --user pdfplumber`.

## Step 3 -- Map the document structure before transcribing anything

`grep -n "^Pytanie\|Dodatek"` on the extracted questions text tells you,
in seconds: total question count, whether there's an appendix block, and
where each question starts. Do this before writing any content -- it's
much cheaper to discover "this set has no appendix" or "this set has 66
questions not 40" now than to find out halfway through transcription.

## Step 4 -- Pull the answer key table

The answers PDF has a compact "Klucz odpowiedzi" table: one row per
question with the correct letter(s), learning objective, and K-level. Grep
for it in your extracted text. This gives you the correct-answer letters
and LO/K-level for the *entire* set in one pass, which you'll transcribe
into each question's `# metadata` block, rather than having to re-derive
them per-question from the prose justification.

## Step 5 -- Don't trust that table blindly -- cross-check it

The "Klucz odpowiedzi" summary table is sometimes hand-typed separately
from the rest of the document and drifts from it -- a wrong K-level or
wrong LO on one specific row is a real, observed failure mode, not a
hypothetical. Before writing a question's metadata, check it against two
*other* independent sources: the table-of-contents entry in the answers
PDF (`Pytanie N (FL-x.y.z, Kn, 1 pkt)`) and the section header directly
above "Poprawna odpowiedź" in the answers PDF body. When the summary table
disagrees with those two -- and those two agree with *each other* -- trust
the TOC/body pair; two independent hand-typed instances agreeing beats one
outlier. When all three agree, there's nothing to resolve.

The correct-answer *letter* (as opposed to LO/K-level) is much less prone
to this kind of drift in practice, but it costs nothing to eyeball it
against the body's "Poprawna odpowiedź: X" line while you're there anyway.

## Step 6 -- Diagrams, charts, and complex tables: read the image, not the text

State diagrams, control-flow graphs, bar charts, and dependency graphs with
arrows extract as garbled or ambiguous text -- don't guess at the
structure from a jumble of coordinates and labels. Render the actual PDF
page as an image and read it directly:

```python
import pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        if "Pytanie nr 23" in (page.extract_text() or "") and i > 5:  # skip the TOC hit
            page.to_image(resolution=200).save(f"q23_page_{i}.png")
```

Then view the image and transcribe the diagram faithfully. See
`references/markdown-conventions.md` for which text form fits which kind of
diagram (transition-table vs bullet-list-of-transitions vs small data
table) -- the right form depends on what the diagram actually is, there's
no one-size-fits-all encoding.

After transcribing, **verify your reading before moving on**: recompute
the question's expected answer from your transcription by hand (count the
edges, trace the state transitions, read the bar heights) and confirm it
lands on one of the four options and matches the reasoning in the answers
PDF's justification. A transcription that "looks plausible" but produces
the wrong answer when you work through it is wrong, silently, and much
harder to catch later than catching it now.

## Step 7 -- Fix obvious source typos, flag genuine ambiguity

Official PDFs aren't perfect. Two patterns come up often enough to name:

- **Duplicate option letters** -- two options both labeled `a)` where the
  second is obviously meant to be `d)` (check: does the correct-answer
  letter from step 4/5 actually correspond to a real, unique option?). Fix
  silently, it's an unambiguous lettering slip.
- **Missing question stems** -- a previous transcription pass sometimes
  dropped the closing question line before the answer options (you'll
  notice this in step 1, comparing existing content against the new PDF).
  Fix by adding the missing line back.

Don't silently "fix" things that might be genuine content errata rather
than transcription slips -- a duplicated sentence in a justification, or a
correct-answer key that seems to contradict its own question. Those are
worth transcribing faithfully and mentioning to the user at the end rather
than editing around, since silently smoothing over a real error in the
official source hides something the user (an ISTQB EC member, in this
repo's case) may want to raise upstream.

## Step 8 -- Draft new content as Python data, not hand-typed markdown

Build a dict of `question_number -> {lo, k, points, question, answers,
explanation, correct, additional}` in a scratch `.py` file, using normal
multi-line Python strings for the prose. This sidesteps manual markdown
escaping mistakes and lets you batch-review ~15-20 questions at a time
before writing anything into the real file. Keep the batches on the
smaller side -- a single 40-question script is unwieldy to review; three
or four scripts of ~10-15 questions each, run in sequence, is easier to
get right and easier to fix if one question needs a redo.

Follow `references/markdown-conventions.md` for house style (dashes,
italics, tables, blockquotes, math, roman lists) while drafting -- getting
this right the first time is much cheaper than reformatting after the fact.

## Step 9 -- Append into the existing file, byte-exactly

Read the target file's exact trailing bytes first:

```python
data = open(md_path, "rb").read()
print(repr(data[-20:]))
```

If it ends `...---\n\n`, a previous author already left the separator for
you -- your first new block goes right after, no extra separator needed.
If it ends in a bare `\n\n` (no `---`), the last existing question assumed
it was final -- you need to prepend `---\n\n` before your first new block
yourself. Getting this wrong either doubles a blank line or (worse) glues
two questions together with no separator, and both are easy to miss on a
casual read but show up immediately as unexpected diff noise in step 12.

Build the full appendix string in one shot and append (open in `"at"` /
append or just concatenate-and-rewrite) -- don't try to interleave writes
per-question.

## Step 10 -- Apply the step-7 fixes as a separate edit

Do the "fix existing content" edits (missing stems, typos) as their own
targeted `Edit` calls *before* appending new content. This keeps the final
diff readable: a reviewer (or you, in step 12) can tell at a glance which
lines are "small correction to something that already existed" versus
"brand new content," instead of it all blurring into one large addition.

## Step 11 -- Validate with the real parser

Don't eyeball the result -- run it through the actual upstream parser:

```bash
python3 .claude/skills/istqb-sample-exam-update/scripts/validate_questions_md.py \
    sample-exam-pl/sample-exam-pl-<letter>/questions-<letter>-pl.md --max 40
```

(Bump `--max` to 66 for sets with an appendix.) This downloads and runs the
*actual* `_read_md_questions` function from `istqb_product_base` -- so a
clean pass means the real CI build will parse the file the same way,
rather than just "looks right to a human." It also prints a
`(number, LO, K-level, correct)` table at the end -- diff that by eye
against the "Klucz odpowiedzi" table from step 4 as a final cross-check.

If it fails on a missing dependency, `python3 -m pip install --user pyyaml yamale`.

## Step 12 -- Review the diff before calling it done

```bash
git diff --stat -- sample-exam-pl/sample-exam-pl-<letter>/
git grep -n -E '^(<<<<<<<|=======|>>>>>>>)' -- sample-exam-pl/sample-exam-pl-<letter>/
```

Insertions should be concentrated in the new content plus the specific
step-10 fixes. If existing questions show up as changed/reformatted when
you didn't intend to touch them, that's the tell for a step-9 boundary bug
-- go back and check the exact bytes at the join point rather than
patching around the symptom.

## Step 13 -- Update metadata.yml

Bump `version` to match the PDF's own stated version ("wersja 1.7" ->
`v1.7`), `compatibility` to the syllabus version the PDF header states
(usually `Compatible with Syllabus v4.0.1`), and `date` to the PDF's
revision date. Only touch the set you actually updated -- don't bump
sibling sets' metadata just because they happen to share a syllabus
version.

## Step 14 -- Clean up

```bash
rm -f sample-exam-pl/sample-exam-pl-<letter>/questions.yml
```

It's gitignored and regenerated at build time, so it never shows up in
`git status` regardless -- this is purely about not leaving a stray local
file that could confuse a later session into thinking it's meaningful.

## Step 15 -- Report back concisely

Tell the user, briefly: what was fixed in already-existing content (and
why -- typo vs missing line), how many questions were added, which
questions needed image-based diagram transcription, any source-document
errata you found and *didn't* silently fix (per step 7 -- flag these,
don't bury them), and the metadata.yml version bump. Skip restating the
mechanical steps you took; the user cares about the outcome and anything
that needs their judgment, not a replay of the process.
