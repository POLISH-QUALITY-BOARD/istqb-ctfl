# Appendix C – Release Notes 

ISTQB® Foundation Syllabus v4.0.1 is an errata for Foundation Level Syllabus v4.0. This errata contains the following changes.

**Changes in Learning Objectives wording**, to align it with the glossary terms

* FL-1.4.1: Summarize the different test activities and tasks -> Explain the different test activities and related tasks
* FL-2.1.5: Explain the shift-left approach -> Explain shift left
* FL-3.1.1: Recognize types of products that can be examined by the different static test techniques -> Recognize types of work products that can be examined by static testing
* FL-3.1.3 Compare and contrast static and dynamic testing -> Compare and contrast static testing and dynamic testing
* FL-4.1.1: Distinguish black-box, white-box and experience-based test techniques -> Distinguish black-box test techniques, white-box test techniques and experience-based test techniques
* FL-5.2.3: Explain how product risk analysis may influence thoroughness and scope of testing -> Explain how product risk analysis may influence thoroughness and test scope

**Text changes to align it with the glossary terms** (artifacts, documentation -> work products, level of risk -> risk level, goals, objectives of testing, test project objectives -> test objectives, test monitoring and control -> test monitoring and test control, test documentation -> testware, iterative and incremental development models -> iterative development models and incremental development models, test environment elements -> test environment items, software quality characteristics -> quality characteristics, test progress and completion reports -> test progress reports and test completion reports, test independence -> independence of testing, stage -> phase, component and component integration testing -> component testing and component integration testing, performance -> performance efficiency, contractual and regulatory acceptance testing -> contractual acceptance testing and regulatory acceptance testing, white box -> white-box, entry/exit criteria -> entry criteria or exit criteria, organizational test policy -> test policy, shift-left, shift-left approach, shift-left strategy -> shift left, types of tests -> test types, control of the testing -> test control, stage of testing -> test activity, reporting on test progress -> test progress reporting, reporting on testing for a completed project -> test completion reporting, false positive -> false-positive result, step -> test step, scope of testing -> test scope, Test design and implementation tools -> Test design and test implementation tools, static and dynamic testing -> testing static and dynamic testing)

**Update of ISO 25010**. A new version of the ISO 25010 standard was published in 2023. It renames “usability” to “interaction capability”, "portability” to flexibility, and adds a new characteristic “safety”. We stay with the original characteristics' names, but we add the new names for usability and portability in section 2.2.2

Three keywords added (test process and traceability in Chapter 1, test strategy in Chapter 5)

#### Corrections in the text

* In 1.1.2 “cause” and “root cause” replaced with “defect”
* In 1.4.1 the description of the activities made clearer and unambiguous
* In 1.4.3 “automated test scripts” changed in “manual and automated test scripts”
* In 1.4.4 detected in “detected defects” removed
* In 1.2.2 “QC” replaced with “testing”, because the section compares QA with testing, not with QC
* In 2.1.3 “test cases are then automatically translated” replaced with “test cases should then be automatically translated” in the context of BDD
* In 2.1.5 “the perspective of testing” changed in “the perspective of testers”
* In 2.1.6 “post-project meetings” removed
* In 2.2.2 the description of the test basis changed from “documentation external to the test object” to “documentation not related to the internal structure of the test object”, to show better the contrast between black-box testing and white-box testing. As well we removed system test as example for start early in the SDLC
* In 3.1 business representatives was specified in more detail
* In 3.1.2 “certain” added to “code defects can be detected using static analysis more efficiently than in dynamic testing”. The previous text suggested that this regards all possible code defects
* In 3.2.2 “a couple of times” replaced with “multiple times” because for large documents a couple of times is not enough
* In 4.2.1 “test object” replaced with “test item”, because this is the proper term in the context of applying test techniques
* In 4.2.1 added that invalid equivalence partitions should be tested in isolation to avoid defect masking
* In 4.2.4 “visited states” replaced with “exercised states”, since “exercise” is the proper term in the context of covering the model elements by test cases
* In 4.2.4 “state transition diagram” replaced with “state diagram”, as this is the common name of this model in computer science, and also to be consistent with the Model-based testing syllabus
* In 5.1.1 “constraints” in the first bullet point removed, constraints are the focus of the second bullet point
* In 5.1.3 “completion criteria” is used in the context of binary “yes/no” criteria, not as a synonym of “exit criteria”, so the appropriate term was changed
* In 5.1.6 the relation between test pyramid layers and test isolation levels is corrected (the higher the layer, the lower is the test isolation). As well we replaced “a reasonable coverage” with “a reasonable level of coverage”
* In 5.5 “anomalies” exchanged with “defects or anomalies”
* In 6.2 “defect rate” replaced with “failure rate” and “that are too complicated for humans to derive” replaced by “that are too complicated for humans to determine"

Moreover, several typos were fixed and some terms were unified across the whole syllabus (e.g., conduct -> perform).


#### RELEASE NOTES FOR THE 4.0 VERSION

ISTQB® Foundation Syllabus v4.0 is a major update based on the Foundation Level syllabus (v3.1.1) and the Agile Tester 2014 syllabus. For this reason, there are no detailed release notes per chapter and section. However, a summary of principal changes is provided below. Additionally, in a separate Release Notes document, ISTQB® provides traceability between the learning objectives (LO) in the version 3.1.1 of the Foundation Level Syllabus, 2014 version of the Agile Tester Syllabus, and the learning objectives in the new Foundation Level v4.0 Syllabus, showing which LOs have been added, updated, or removed.

At the time the syllabus was written (2022-2023) more than one million people in more than 100 countries have taken the ISTQB® Foundation Level exam, and more than 800,000 are certified testers worldwide. With the expectation that all of them have read the Foundation Syllabus to be able to pass the exam, this makes the Foundation Syllabus likely to be the most read software testing document ever! This major update is made in respect of this heritage and to improve the views of hundreds of thousands more people on the level of quality that ISTQB® delivers to the global testing community.

In this version all LOs have been edited to make them atomic, and to create one-to-one traceability between LOs and syllabus sections, thus not having content without also having a LO. The goal is to make this version easier to read, understand, learn, and translate, focusing on increasing practical usefulness and the balance between knowledge and skills.

This major release has made the following changes:

* Size reduction of the overall syllabus. Syllabus is not a textbook, but a document that serves to outline the basic elements of an introductory course on software testing, including what topics should be covered and on what level. Therefore, in particular:
  * In most cases examples are excluded from the text. It is a task of a training provider to provide the examples, as well as the exercises, during the training
  * The “Syllabus writing checklist” was followed, which suggests the maximum text size for LOs at each K-level (K1 = max. 10 lines, K2 = max. 15 lines, K3 = max. 25 lines)
* Reduction of the number of LOs compared to the Foundation Level v3.1.1 and Agile v2014 syllabi
  * 14 K1 LOs compared with 21 LOs in FL v3.1.1 (15) and AT 2014 (6)
  * 42 K2 LOs compared with 53 LOs in FL v3.1.1 (40) and AT 2014 (13)
  * 8 K3 LOs compared with 15 LOs in FL v3.1.1 (7) and AT 2014 (8)
* More extensive references to classic and/or respected books and articles on software testing and related topics are provided
* Major changes in chapter 1 (Fundamentals of Testing)
  * Section on testing skills expanded and improved
  * Section on the whole team approach (K1) added
  * Section on the independence of testing moved to Chapter 1 from Chapter 5
* Major changes in chapter 2 (Testing Throughout the SDLCs)
  * Sections 2.1.1 and 2.1.2 rewritten and improved, the corresponding LOs are modified
  * More focus on practices like: test-first approach (K1), shift left (K2), retrospectives (K2)
  * New section on testing in the context of DevOps (K2)
  * Integration testing level split into two separate test levels: component integration testing and system integration testing
* Major changes in chapter 3 (Static Testing)
  * Section on review techniques, together with the K3 LO (apply a review technique) removed
* Major changes in chapter 4 (Test Analysis and Design)
  * Use case testing removed (but still present in the Advanced Test Analyst syllabus)
  * More focus on collaboration-based approach to testing: new K3 LO about using ATDD to derive test cases and two new K2 LOs about user stories and acceptance criteria
  * Decision testing and coverage replaced with branch testing and coverage (first, branch coverage is more commonly used in practice; second, different standards define the decision differently, as opposed to “branch”; third, this solves a subtle, but serious flaw from the old FL2018 which claims that „100% decision coverage implies 100% statement coverage” – this sentence is not true in case of programs with no decisions)
  * Section on the value of white-box testing improved
* Major changes in chapter 5 (Managing the Test Activities)
  * Section on test strategies/approaches removed
  * New K3 LO on estimation techniques for estimating the test effort
  * More focus on the well-known Agile-related concepts and tools in test management: iteration and release planning (K1), test pyramid (K1), and testing quadrants (K2)
  * Section on risk management better structured by describing four main activities: risk identification, risk assessment, risk mitigation and risk monitoring
* Major changes in chapter 6 (Test Tools)
  * Content on some test automation issues reduced as being too advanced for the foundation level – section on tools selection, performing pilot projects and introducing tools into organization removed