# Formatting conventions for questions-<letter>-pl.md

This file is hand-authored markdown, not machine-generated, but it does get
parsed by the real `istqb_product_base` toolchain (see `scripts/validate_questions_md.py`),
so the structure below is not optional even though the styling choices are yours to make
consistently.

## Block structure

Every question is one block:

```
# metadata
lo: FL-x.y.z
k-level: K1
points: 1
correct: c
[additional: true]

## question
<question text>

## answers
a) ...
b) ...
c) ...
d) ...

## justification
a) ...
b) ...
c) ...
d) ...
```

Notes:
- `additional: true` is only ever written for appendix ("Dodatek A") questions.
  For ordinary questions, omit the line entirely rather than writing
  `additional: false` -- the parser defaults missing to false, and every
  existing block in the file follows the omit convention. Don't introduce
  the false-writing variant partway through a file.
- `correct:` is a plain comma-separated scalar (`c` or `a, e`), not a YAML
  flow list (`["c"]` or `[a, e]`). This looks unconventional but it's what
  the whole file already does and what the parser expects on this side of
  the pipeline.
- Blocks are separated by: blank line, a line containing only `---`, blank
  line. The **last** question in the file has no trailing separator -- if
  you're appending, check whether the file currently ends with `---\n\n`
  (meaning a previous author already left the separator for you) or a bare
  `\n\n` (meaning you need to add the `---\n\n` yourself before your first
  new block). Get this wrong and you'll either double a blank line or glue
  two questions' worth of content together with no separator -- both break
  the parser silently is not the failure mode; it usually still parses but
  produces a diff that reformats existing content, which is the tell that
  something's off (see SKILL.md step "diff review").

## Prose and typography

The file already has an established house style; match it rather than
introducing a new one partway through:

- **Dashes**: write en/em dashes as literal `--` (two hyphens), never a
  Unicode – or — character. Pandoc converts `--` to a proper en-dash at
  build time; a literal Unicode dash in the source just looks inconsistent
  next to everything else.
- **Italics**: single `*asterisks*`, not `_underscores_`. This matters
  functionally, not just stylistically -- CommonMark's underscore-emphasis
  rules get confused by literal underscores inside the emphasized text
  (e.g. a username like `test_admin01` inside an italicized sentence), so
  asterisks are the safe choice and it's what the file already uses.
- **Bold**: `**double asterisks**`, used for the emphasized qualifier words
  ISTQB questions lean on heavily -- "najlepiej", "NAJLEPIEJ", "wyłącznie",
  "dwa", "najmniej". Don't guess which words are bold from how the sentence
  reads in English -- the source PDF's actual bold formatting is
  authoritative and is often specific (only "dwa" bold, not "dwa z
  poniższych"). See SKILL.md step 2 for how to extract this reliably instead
  of eyeballing the PDF.
- **Roman-numeral sub-lists** (`i. ii. iii. ...`, used constantly for
  multi-part "which of the following are true" questions): plain lines
  `i. Some statement`, one per line, no markdown bullet prefix. This matches
  the existing convention and also matches how the lettered options
  (`a) b) c)`) are written, keeping the visual style consistent between the
  two list types used side by side in the same question.

## Tables

Decision tables, state-transition tables, and any other grid the PDF
presents as an actual table: use GFM pipe-table syntax with `**Header**`
cells bolded, e.g.:

```
| | **R1** | **R2** | **R3** |
| :--- | :---: | :---: | :---: |
| C1: Wiek | 0--18 | 19--65 | >65 |
```

Left-align label columns (`:---`), center data columns (`:---:`) -- this
matches how the source PDFs visually present these tables and reads more
naturally than left-aligning everything.

## Blockquotes

Scenario text meant to be read as a "quoted document" inside a question --
defect reports, test-plan excerpts, execution logs, user-story text in
Given/When/Then form -- goes in a `>` blockquote, with field labels bolded
inline:

```
> **Identyfikator usterki**: 001 **Tytuł**: Nie można zwrócić książki
>
> **Opis**: ...
```

This distinguishes "this is a document the tester is looking at" from "this
is the question's own prose," which matters for readability once these get
typeset.

## Math

Formulas destined for the pandoc -> LaTeX pipeline (three-point estimation,
branch coverage ratios, iteration effort extrapolation, etc.) use inline
LaTeX math: `$E = (a + 4 \cdot m + b) / 6$`, `$\dfrac{3 \cdot A(n-1) +
A(n-2)}{4}$`. Don't transcribe the PDF's Unicode math-italic characters
(𝐸, 𝑛, ⋅) literally -- they're a rendering artifact of the PDF's font, not
meaningful content, and LaTeX math mode is both more faithful to what the
source document actually means and safe to round-trip through the build.

## Diagrams that aren't tables or formulas

State diagrams, control-flow graphs, and dependency graphs with arrows
don't have a single canonical text form -- pick whichever of these reads
most naturally for the specific diagram, and stay consistent within one
question:

- **State diagrams with guards/actions** (e.g. `Add [N<2] / N:=N+1`): a
  bullet list of transitions, `Source --event [guard] / action--> Target`,
  one per line.
- **Plain state-transition tables** (rows = states, columns = events, cell
  = target state): a markdown table, states down the left, events across
  the top -- this is usually a more faithful transcription than prose when
  the PDF itself presents it as a grid.
- **Control-flow graphs** (unlabeled circles/boxes connected by arrows,
  used for branch-coverage counting questions): number the nodes yourself
  in a sentence ("węzeł 1 to punkt wejścia... zawiera następujące
  krawędzie: 1->2, 2->3, ...") and state the total edge count explicitly --
  the question is usually *asking* for that count, so getting it right and
  showing your work matters more than picking a particular notation.
- **Dependency graphs among test cases** (TC1 -> TC2 -> TC5, etc.,
  sometimes with priorities attached): a small table (test case / priority
  / depends-on) is almost always clearer than prose and easier to verify
  against the image than a sentence describing arrows.

Whichever form you pick, see SKILL.md's diagram-transcription step for how
to verify you read it correctly before committing to a transcription.
