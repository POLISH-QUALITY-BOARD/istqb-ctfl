# metadata
lo: 1.2.1
k-level: K2
points: 1
correct: d

## question
Which of the following is an example of why testing is necessary?

## answers
a) Dynamic testing increases quality by causing test objects to fail in ways that could never be achieved by the users  
b) Static testing is used by developers to identify failures in their program code earlier than can be achieved through dynamic testing  
c) Static analysis provides evidence to customers that the elements of the system that provide no outputs are fit for release  
d) Reviews increase the quality of requirements specifications and lead to fewer changes being needed in derived work products  

## justification
a) Is not correct. It is often possible to use dynamic testing to cause a test object to fail in ways that could never be achieved by the users, such as by using fault injection. However, if the failure can never occur with real end users, then identifying it is not especially valuable as testing is ultimately aimed at improving the work product for the end users. Spending time testing for failures that cannot occur with real users is not an efficient use of a tester’s time  
b) Is not correct. Static testing in the form of static analysis is used by developers to identify defects in their program code earlier than can be achieved through dynamic testing. Note, however, that static testing (and static analysis) is used to detect defects, not failures, which are found by dynamic testing. Thus it is the use of the term ‘failures’ that makes this an incorrect option  
c) Is not correct. Static analysis directly detects anomalies in code, which may be defects, and this is normally for the developer, not the customer. The provision of evidence for release by the use of static analysis of elements that provide no output is nonsense  
d) Is correct. Reviews are a form of static testing that can be applied from the very start of the software development lifecycle and are used to find defects that can be removed before subsequent development activities waste effort on faulty requirements. If the defects are not detected and removed early on, then when the defect is found derived work products, such as the design and code, will need to be changed as they were based on faulty requirements  

# metadata
lo: 1.2.2
k-level: K1
points: 1
correct: b

## question
Which of the following statements about quality assurance (QA) and/or quality control (QC) is correct?

## answers
a) QA is performed as part of testing  
b) St Testing is performed as part of QC  
c) Testing is another term for QC  
d) Testing is performed as part of QA  

## justification
a) Is not correct. The statement ‘QA is performed as part of testing’ is incorrect because QA concentrates on process improvement and implementation, using a preventive approach to avoid errors and defects, while testing is a form of QC that is used to detect defects  
b) Is correct. The statement ‘Testing is performed as part of QC’ is correct because QC aims to achieve appropriate levels of quality by focusing on identifying and correcting product defects. Testing is a significant part of QC and helps to uncover these defects  
c) Is not correct. The statement ‘Testing is another term for QC’ is incorrect because although testing is a significant part of QC and helps to uncover defects, other (non-testing) techniques utilized in QC include formal methods like model checking and proof of correctness, as well as simulation and prototyping  
d) Is not correct. The statement ‘Testing is performed as part of QA’ is incorrect because QA concentrates on process improvement and implementation, using a preventive approach to avoid errors and defects, while testing is a form of QC that is used to detect defects  

# metadata
lo: 1.3.1
k-level: K2
points: 1
correct: d

## question
One of the ‘principles of testing’ states that exhaustive testing is impossible. Which of the following is an example of addressing this principle in practice?

## answers
a) Creating test cases that cover every possible specified output  
b) Documenting all possible test input variations and prioritizing these based on importance  
c) Starting testing as early as possible with reviews and other static testing approaches  
d) Using equivalence partitioning and boundary value analysis to generate test cases  

## justification
The ‘exhaustive testing is impossible’ principle is concerned with the fact that it is not feasible to test every possible variation of test inputs in all different circumstances, except in trivial cases. Instead, testing utilizes test techniques, test case prioritization, and risk-based testing to sample from the set of possibilities and focus testing efforts.

a) Is not correct. The principle states that it is not feasible to test everything except in trivial cases. Testing everything would require testing every possible variation of test inputs in all different circumstances, which is generally infeasible as there will be a practically infinite number. Testing every possible specified output will not address this problem as the relationship between inputs and specified outputs can be different for each test object. Sometimes there may be a practically infinite number of possible specified outputs (e.g., when there are several variables representing real numbers), whereas at other times there may be just two specified outputs, such as with a single variable that can be either true or false  
b) Is not correct. The principle states that it is not feasible to test every possible variation of test inputs in all different circumstances. This is because for non-trivial systems there is a practically infinite number. Therefore, in practice, documenting all possible test input variations would be impractical as it would take an infinite length of time  
c) Is not correct. Starting testing as early as possible with reviews and other static testing approaches will not address the problem of there being too many possible test cases. The ‘early testing saves time and money’ principle is concerned with fixing defects early on to prevent the occurrence of subsequent defects in derived work products, thereby reducing costs and the likelihood of failures  
d) Is correct. The use of equivalence partitioning and boundary value analysis to generate test cases is one way to address the principle as these test techniques provide a systematic way to derive a finite subset of all possible test cases  

# metadata
lo: 1.4.1
k-level: K2
points: 1
correct: a

## question
Which test activity involves working with test data requirements, test conditions, test environment requirements and test cases?

## answers
a) Test design  
b) Test execution  
c) Test analysis  
d) Test implementation  

## justification
a) Is correct. Test design involves using test conditions to create test cases and other necessary testware, such as test data requirements and test charters for exploratory testing. Test environment requirements are also specified, including the necessary infrastructure and tools  
b) Is not correct. Test execution involves executing test cases (as part of test procedures), however it does not directly cover the other testware mentioned in the question, such as test data requirements, test environment requirements and test conditions  
c) Is not correct. Test analysis is used to identify the features that require testing. The test basis is analyzed and defined as test conditions, which are then prioritized along with related risks. While this activity involves working with test conditions, it does not cover the other testware mentioned in the question, such as test data requirements, test environment requirements and test cases  
d) Is not correct. Test implementation includes the generation of test procedures, such as manual and automated test scripts, which are created from test cases and may be assembled into test suites. Test procedures are prioritized and arranged in a test execution schedule. Test data is created, and the test environment built, and its set up verified. While this activity involves explicitly working with test cases, and may use test data requirements and test environment requirements to create test data and the test environment, it does not cover test conditions  

# metadata
lo: 1.4.2
k-level: K2
points: 1
correct: c

## question
Which of the following is MOST likely to impact how testing is performed for a given test object?

## answers
a) The average level of experience of the organization’s marketing team  
b) The knowledge of users that a new system is being developed for them  
c) The number of years’ experience of the members of the test team  
d) The end user’s organizational structure for a commercial music streaming application  

## justification
a) Is not correct. The organization’s marketing team is unlikely to perform much testing (although in some organizations they may be involved with acceptance testing), so their average level of experience (most of which would be in marketing) is not likely to impact how testing is performed for a given test object  
b) Is not correct. The level of knowledge of users that a new system is being built for them is unlikely to affect how testing is performed. Any user involvement that could affect how testing is performed is more likely to be as a result of decisions made by the testers, customer and project manager  
c) Is correct. The number of years’ experience of the members of the performance testing team will help to determine the capabilities and knowledge (e.g., of different tools and defect types) that the team members will apply when they are testing  
d) Is not correct. The organizational structure of the different end users (who may be varied) will change between users. So, it may not even be known when the application is being tested, and the end user’s organizational structure can thus have little effect on how the testing is performed  

# metadata
lo: 1.4.4
k-level: K2
points: 1
correct: b

## question
Which of the following statements is a CORRECT example of the value of traceability?

## answers
a) Traceability between the mitigated risks and passing test cases provides a means of determining the level of residual risk  
b) Traceability between user requirements and test execution results provides a means of measuring project progress against business goals  
c) Traceability between testers and failing test cases provides a means of determining the skill level of the testers  
d) Traceability between the identified risks and written test conditions provides a means of determining which risks are worth testing  

## justification
a) Is not correct. Traceability between the mitigated risks and passing test cases provides little information, because to be mitigated (by testing) the risks would need to have a corresponding passing test case. To be able to assess residual risk, traceability between all risks and test results needs to be available, so that the risks that do not have a corresponding passing test can be identified as the residual risks  
b) Is correct. Traceability between user requirements and test execution results provides an indication of which user requirements have been tested and so provides a means of measuring project progress (in the context of testing) against business goals  
c) Is not correct. It is not clear that failing test cases provide an indication of tester skills any more than passing test cases. It would partly depend on the test objective (e.g., building confidence or causing failures). Also, such measurement of testers based on passing and failing test cases can be counter-productive as it could cause the testers to optimize their testing based on that metric rather than the test objective  
d) Is not correct. Traceability between the identified risks and written test conditions provides a means of determining which further test conditions need to be written. Determining which risks are worth testing is part of risk management, and risk mitigation in particular  

# metadata
lo: 1.5.1
k-level: K2
points: 1
correct: b

## question
Which of the following is MOST likely to be an example of a tester using a generic skill when testing?

## answers
a) The tester’s deep knowledge of a variety of computer games meant that they got on well with one of the developers who was also into gaming  
b) The tester was a former pilot and was better able to understand the acceptance criteria for the helicopter control system  
c) The tester previously worked as a programmer and used their skills in this area to better communicate with the business analysts  
d) The tester was very careful not to make mistakes when they methodically generated test cases prior to starting their exploratory testing session  

## justification
a) Is not correct. Strong communication skills, active listening, and teamwork abilities enable a tester to interact effectively with all stakeholders, however a deep knowledge of a variety of computer games that allowed them to get on well with one developer is not an example of a generic skill useful to testers  
b) Is correct. Domain knowledge that can be used to understand and communicate with end-users and business representatives is one of the generic skills required by testers. A tester with experience as a pilot would make them better able to appreciate the acceptance criteria for the helicopter control system  
c) Is not correct. Although programming skills could be considered as technical knowledge which can increase efficiency when utilizing some test tools, it is unlikely that these skills would improve their communication with business analysts  
d) Is not correct. Although thoroughness, attention to detail, curiosity, and a methodical approach to identifying hard-to-find defects are all useful generic skills for testers, it is doubtful they would be generating test cases prior to starting exploratory testing. This is because one of the main tenets of exploratory testing is that the test cases are generated during the testing, not scripted in advance  

# metadata
lo: 1.5.2
k-level: K1
points: 1
correct: d

## question
Which of the following is an advantage of the whole-team approach?

## answers
a) It allows team members to take on any role at any time  
b) It only needs a single team to support the complete development project  
c) It embeds business representatives alongside developers in the same team  
d) It generates a team synergy that benefits the entire project  

## justification
a) Is not correct. The whole-team approach allows any team member with the requisite skills and knowledge to undertake any task, however that does not mean that team members can take on any role at any time. Typically, they only take on roles in which they are competent, and there is no suggestion that every team member can do every role  
b) Is not correct. The whole-team approach applies to how a single team (typically in Agile software development) works; it does not cover how multiple teams are supposed to work on larger projects, and it does not suggest that only one ‘whole’ team is needed for a complete project  
c) Is not correct. The whole-team approach does not expect every team member to be involved in every important decision. For instance, there is no need for the business representative (i.e. the Product Owner) to be involved in every technical decision that does not affect the business outcome and implementing such an approach would unnecessarily slow down the team’s progress  
d) Is correct. By leveraging the diverse skill sets of each team member most effectively, the whole-team approach fosters superior team dynamics, promotes robust communication and collaboration, and generates a team synergy that benefits the entire project  

# metadata
lo: 2.1.1
k-level: K2
points: 1
correct: b

## question
Which of the following statements about the chosen software development lifecycle is CORRECT?

## answers
a) If agile software development is used, system test automation replaces the need for regression testing  
b) If a sequential development model is used, then the dynamic testing is typically restricted to later in the lifecycle  
c) If an iterative development model is used, then component testing is typically performed manually by developers  
d) If an incremental development model is used, then static testing is done in early increments and dynamic testing in later increments  

## justification
a) Is not correct. In agile software development, deliverables are produced in each iteration, and the frequent delivery of increments necessitates extensive regression testing. Although some (or all) of this regression testing may be automated, the regression testing (automated or not) cannot be replaced by system test automation  
b) Is correct. If a sequential development model is used, then early in the lifecycle no code is available for execution, and so during this time static testing (e.g., reviews) is performed. Later in the lifecycle, when code is available for execution, dynamic testing is possible. Note, however, that preparation for dynamic testing will often occur early in any software development lifecycle  
c) Is not correct. If an iterative development model, like agile software development, is used, then component tests may well be used for regression testing for each iteration. In which case, there is a strong argument for automating these component tests, which will have to be run frequently, and there is unlikely to be a strong argument for developers performing these component tests manually  
d) Is not correct. In most incremental development models, deliverables are produced in each increment, requiring both static and dynamic testing at all test levels for each increment delivered  

# metadata
lo: 2.1.2
k-level: K1
points: 1
correct: b

## question
Which of the following is a good testing practice that applies to all software development lifecycles?

## answers
a) Testers should review work products as part of the next development phase  
b) Testers should review work products as soon as drafts are available  
c) Testers should review work products before test analysis and design begins  
d) Testers should review work products immediately after they are published  

## justification
a) Is not correct. Testers should review work products as soon as drafts are available to enable early testing as part of a shift-left approach. If they waited until the next development phase, then unnecessary development (and test) work could be started on unreviewed, flawed work products  
b) Is correct. Testers should review work products as soon as drafts are available to enable early testing as part of a shift-left approach  
c) Is not correct. Testers typically review work products that form the test basis as part of test analysis, not before test analysis and design  
d) Is not correct. Testers should review work products as soon as drafts are available to enable early testing as part of a shift-left approach. Waiting until they are published means that any defects that could be found by tester review will be in the published document  

# metadata
lo: 2.1.3
k-level: K1
points: 1
correct: a

## question
Which of the following is an example of a test-first approach to development?

## answers
a) Test-Driven Development  
b) Coverage-Driven Development  
c) Quality-Driven Development  
d) Feature-Driven Development  

## justification
a) Is correct. Test-Driven Development (TDD) is a well-known example of a test-first approach to development  
b) Is not correct. Coverage-Driven Development is not a correct example of a test-first approach to development  
c) Is not correct. Quality-Driven Development is not a correct example of a test-first approach to development  
d) Is not correct. Feature-Driven Development is not an example of a testfirst approach to development, but is, instead, an agile software development methodology based around delivering features (as opposed to user stories in Scrum)  

# metadata
lo: 2.1.4
k-level: K2
points: 1
correct: b

## question
Which of the following statements about DevOps is CORRECT?

## answers
a) To speed up releases, continuous integration is used to encourage developers to submit code quickly without the need to complete component testing  
b) To be able to update and release systems on a more frequent basis, many automated regression tests are required to reduce the danger of regression  
c) To treat both developers and operations equally, the testers will allocate more effort to release testing by operations using a shift-right approach  
d) To create increased synergy between testers, developers and operations, the testing must become fully automated with no manual testing  

## justification
a) Is not correct. DevOps enhances testing in several ways, such as by providing fast feedback on code quality, automated regression testing that minimizes regression risk, and promoting a shift-left approach with high-quality code submission and component tests. This is largely provided through continuous integration, where the developers submit component (unit) tests with their new code, which must pass for the code to be admitted to the build. Therefore, developers do need to complete component testin  
b) Is correct. DevOps enhances testing in several ways, such as by providing fast feedback on code quality, automated regression testing that minimizes regression risk, and promoting a shift-left approach with high-quality code submission and component tests  
c) Is not correct. DevOps enhances testing in several ways, such as by providing fast feedback on code quality, automated regression testing that minimizes regression risk, and promoting a shift-left approach with high-quality code submission and component tests. Testers do not attempt to treat developers and operations equally by spending more time on release testing, although a shift-right approach to testing (testing in production) may well be used  
d) Is not correct. Automated processes like continuous integration/continuous delivery (CI/CD) in DevOps facilitate stable test environments and reduce the need for manual testing, however, there is a risk of overlooking the importance of manual testing, especially from a user's perspective  

# metadata
lo: 2.2.1
k-level: K2
points: 1
correct: a

## question
Which of the following is MOST likely to be performed as part of system testing?

## answers
a) Security testing of a credit management system by an independent test team  
b) Testing the interface of a currency exchange system with an external banking system  
c) Beta testing of a remote learning system by courseware developers  
d) Testing interactions between the user interface and database of a human resources system  

## justification
a) Is correct. System testing examines the behavior and capabilities of the complete system and covers non-functional testing of quality characteristics, which includes security testing. This type of testing is often performed by an independent test team based on system specifications  
b) Is not correct. System integration testing examines the interfaces with other systems and external services  
c) Is not correct. Beta testing is a type of acceptance testing performed at an external site by roles outside the development organization  
d) Is not correct. Component integration testing involves testing the (interfaces and) interactions between components of a system, such as the user interface and database  

# metadata
lo: 2.2.3
k-level: K2
points: 1
correct: d

## question
Which of the following statements is CORRECT?

## answers
a) Regression tests increase in number as the project progresses, whereas the number of confirmation tests decreases as the project progresses  
b) Regression tests are created and run when the test object is fixed, whereas confirmation tests are run whenever the test object is enhanced  
c) Regression testing is concerned with checking that the operational environment remains unchanged, whereas confirmation testing is concerned with testing changes to the test object  
d) Regression testing is concerned with adverse effects in unchanged code, whereas confirmation testing is concerned with testing changed code  

## justification
a) Is not correct. Regression tests increase in number as the project progresses, as new regression tests are typically required as changes are made to the system. Similarly, the number of confirmation tests also typically increases as the project progresses as new confirmation tests are needed for each fix made to a system  
b) Is not correct. It is the other way round. Confirmation tests are created and run when the test object is fixed, and regression tests are (ideally) run whenever the test object is enhanced (changed)  
c) Is not correct. Confirmation testing verifies that a defect has been fixed correctly and so is concerned with testing changes to the test object. However, regression testing ensures that changes (including changes to the operational environment) do not have negative effects on unchanged software and so does not check that the operational environment remains unchanged  
d) Is correct. Regression testing ensures that changes do not have negative effects on unchanged software. Confirmation testing verifies that a defect has been fixed – and so is concerned with changed code  

# metadata
lo: 3.1.3
k-level: K2
points: 1
correct: b

## question
Which of the following is an example of a defect that can be found by static testing but NOT by dynamic testing?

## answers
a) Lack of usability provided through the user interface  
b) Code with no path that reaches it  
c) Poor response times for most of the expected users  
d) Required features that are not implemented in the code  

## justification
a) Is not correct. A lack of usability provided through the user interface can be detected through a review using a suitable checklist, but the lack of usability can also be identified by getting several typical users to dynamically test the user interface and provide feedback on its usability  
b) Is correct. A code review can detect code that cannot be reached by any path, however dynamic tests can only exercise reachable code and cannot determine that code cannot be reached without running every possible combination of inputs and input states, which is impractical for real code  
c) Is not correct. Poor response times for most of the expected users are difficult to determine without executing the code (i.e., by static testing), so in this situation dynamic testing could find a defect, but static testing is unlikely to find it  
d) Is not correct. A review of the code by someone who is aware of the required features could detect that the required features had not been implemented in the code, and dynamic testing could also be used to determine that these required features had not been implemented  

# metadata
lo: 3.2.1
k-level: K1
points: 1
correct: c

## question
Which of the following is a benefit of early and frequent stakeholder feedback?

## answers
a) Managers are aware of which developers are less productive  
b) It allows project managers to prioritize their stakeholder interactions  
c) It facilitates early communication of potential quality issues  
d) End users better understand why the delivery of the work product is delayed  

## justification
a) Is not correct. The feedback is from stakeholders (e.g., business representative, end user), not from developers, so this feedback is not likely to inform managers which developers are more or less productive  
b) Is not correct. Early and frequent feedback from stakeholders is not used by project managers to prioritize how they interact with the different stakeholders  
c) Is correct. Obtaining feedback from stakeholders early and often in the software development process can be highly beneficial as it facilitates early communication of potential quality issues, can prevent misunderstandings about requirements, and ensures that any changes in stakeholder requirements are understood and implemented sooner  
d) Is not correct. Early and frequent feedback can prevent the development of a product that does not meet stakeholder needs, and results in costly rework and missed deadlines, so, ideally there should be no delay. Also, the feedback is from stakeholders (not to them), which includes the end users, so the end users providing feedback will not aid the end users’ understanding  

# metadata
lo: 3.2.2
k-level: K2
points: 1
correct: d

## question
Given the following task descriptions:

1. The quality characteristics to be evaluated and the exit criteria are selected
2. Everyone has access to the work product
3. Anomalies are identified in the work product
4. Anomalies are discussed

And the following review activities:

A. Individual review 
B. Review initiation 
C. Planning
D. Communication and analysis

Which of the following BEST matches the task descriptions and activities?

## answers
a) 1B, 2C, 3D, 4A  
b) 1B, 2D, 3C, 4A  
c) 1C, 2A, 3B, 4D  
d) 1C, 2B, 3A, 4D  

## justification
Considering each of the listed task descriptions:

1. The quality characteristics to be evaluated and the exit criteria are selected - (Planning (C): Defining the review scope, purpose, work product to be reviewed, quality characteristics to be evaluated, areas of focus, exit criteria, supporting information such as standards, effort, and timeframes.)
2. Everyone has access to the work product - (Review initiation (B): Ensuring all participants have access to the work product and necessary resources, and clarifying their roles and responsibilities.)
3. Anomalies are identified in the work product - (Individual review (A): Evaluating the work product's quality, identifying and logging anomalies, recommendations, and questions using review techniques like checklist-based and scenario-based reviewing.)
4. Anomalies are analyzed and discussed - (Communication and analysis (D): Analyzing and discussing each anomaly, determining its status, ownership, and required actions, and making review decisions, normally in a meeting. This could include determining the need for a follow-up review.)

a) Is not correct  
b) Is not correct  
c) Is not correct  
d) Is correct. The correct match is: 1C, 2B, 3A, 4D  

# metadata
lo: 3.2.3
k-level: K1
points: 1
correct: c

## question
Given the following roles in reviews:

1. Scribe
2. Review leader 
3. Facilitator
4. Manager

And the following responsibilities in reviews:

A. Ensures the effective running of review meetings and the setting up a safe review environment
B. Records review information, such as decisions and new anomalies found during the review meeting
C. Decides what is to be reviewed and provides resources, such as staff and time for the review
D. Takes overall responsibility for the review such as organizing when and where the review will take place

Which of the following BEST matches the roles and responsibilities?

## answers
a) 1A, 2B, 3D, 4C  
b) 1A, 2C, 3B, 4D  
c) 1B, 2D, 3A, 4C  
d) 1B, 2D, 3C, 4A  

## justification
Considering each of the listed roles

1. Scribe (or Recorder) - responsible for gathering feedback from reviewers and documenting review information, such as decisions made, and any new anomalies identified during the review meeting. (Records review information, such as decisions and new anomalies found during the review meeting - B)
2. Review Leader - responsible for overseeing the review process, such as selecting the review team members, scheduling review meetings, and ensuring that the review is completed successfully. (Takes overall responsibility for the review such as organizing when and where the review will take place - D)
3. Facilitator (or Moderator) - responsible for ensuring that the review meetings run effectively, including managing time, mediating discussions, and creating a safe environment where everyone can voice their opinions freely. (Ensures the effective running of review meetings and the setting up of a safe review environment - A)
4. Manager - responsible for deciding what needs to be reviewed and allocating resources, such as staff and time, for the review. (Decides what is to be reviewed and provides resources, such as staff and time for the review - C

a) Is not correct  
b) Is not correct  
c) Is correct. The correct match is: 1B, 2D, 3A, 4C  
d) Is not correct  

# metadata
lo: 4.1.1
k-level: K2
points: 1
correct: d

## question
Which of the following statements BEST describes the difference between decision table testing and branch testing?

## answers
a) In decision table testing, the test cases are derived from the decision statements in the code. In branch testing, the test cases are derived from knowledge of the control flow of the test object.  
b) In decision table testing, the test cases are derived from the specification that describes the business logic. In branch testing the test cases are based on anticipation of potential defects in the source code.  
c) In decision table testing, the test cases are derived from knowledge of the control flow of the test object. In branch testing, test cases are derived from the specification that describes the business logic.  
d) In decision table testing, the test cases are independent of how the software is implemented. In branch testing, test cases can be created only after the design or implementation of the code  

## justification
a) Is not correct. Decision table testing is a black-box test technique, so it is specification-based, not structure-based – the test cases are not based on the decisions in the source code. In branch testing, the test cases are derived from knowledge of the control flow of the test objec  
b) Is not correct. Anticipation of potential defects is used in error guessing (an experience-based test technique), not in branch testing (a structurebased technique). In decision table testing, the test cases are derived from the specification that describes the business logic  
c) Is not correct. If a test case is based on the knowledge of the control flow of the test object, it is a white-box test technique. Decision table testing is typically based on an analysis of business logic, so it is a black-box test technique. In branch testing, test cases are not derived from the specification – this would make it a black-box test technique. Branch testing is a white-box test technique, where test cases are derived based on the source code structure  
d) Is correct. Decision table testing is a black-box test technique, so it is based on an analysis of the specified behavior of the test object without reference to its internal structure. Therefore, the test cases are independent of how the software is implemented. Branch testing is a white-box test technique, so test cases are based on an analysis of the test object’s internal structure and processing. As the test cases are dependent on how the software is designed and coded, they can only be created after the design or implementation of the test object  

# metadata
lo: 4.2.1
k-level: K3
points: 1
correct: a

## question
Customers of the TestWash car wash chain have cards with a record of the number of washes they have bought so far. The initial value is 0. After entering the car wash, the system increases the number on the card by one. This value represents the number of the current wash. Based on this number the system decides what discount the customer is entitled to. For every tenth wash the system gives a 10% discount, and for every twentieth wash, the system gives a further 40% discount (i.e., a 50% discount in total). Which of the following sets of input data (understood as the numbers of the current wash) achieves the highest equivalence partition coverage?

## answers
a) 19, 20, 30  
b) 11, 12, 20  
c) 1, 10, 50  
d) 10, 29, 30, 31  

## justification
a) Is correct. 19 covers the “no discount” partition, 20 covers the “50% discount” partition, and 30 covers the “10% discount” partition. These three values cover all three of the valid equivalence partitions  
b) Is not correct. 11 and 12 cover the “no discount” partition, while 20 covers the “50% discount” partition, so covering two of the three valid equivalence partitions  
c) Is not correct. 1 covers the “no discount” partition, while 10 and 50 cover the “10% discount” partition. The “50% discount” partition is not covered, so overall two of the three valid equivalence partitions are covered  
d) Is not correct. 29 and 31 cover the “no discount” partition, while 10 and 30 cover the “10% discount” partition. The “50% discount” partition is not covered, so overall two of the three valid equivalence partitions are covered  

# metadata
lo: 4.2.2
k-level: K3
points: 1
correct: d

## question
You are testing a form that verifies the correctness of the length of the password given as input. The form accepts a password with the correct length and rejects a password that is too short or too long. The password length is correct if it has between 6 and 12 characters inclusive. Otherwise, it is considered incorrect. At first, the form is empty (password length = 0). You apply boundary value analysis to the “password length” variable. Your set of test cases achieves 100% 2-value boundary value coverage. The team decided that due to the high risk of this component, test cases should be added to ensure 100% 3-value boundary value coverage. Which additional password lengths should be tested to achieve this?

## answers
a) 4, 5, 13, 14  
b) 7, 11  
c) 1, 5, 13  
d) 1, 4, 7, 11, 14  

## justification
The domain for the password length has three equivalence partitions

* passwords too short {0, 1, …, 4, 5}
* passwords OK {6, 7, …, 11, 12}
* passwords too long {13, 14, …}

To achieve full coverage for 3-value BVA we need to test the following values: 0, 1, 4, 5, 6, 7, 11, 12, 13, 14.  
Since 2-value BVA is already covered, this means that we have already tested the passwords of length: 0, 5, 6, 12 and 13.   
This means that the additional lengths that need to be covered to move from 2-value to 3-value are: 1, 4, 7, 11 and 14.   

a) Is not correct  
b) Is not correct  
c) Is not correct  
d) Is correct  

# metadata
lo: 4.2.3
k-level: K3
points: 1
correct: b

## question
The following decision table contains the rules for determining the risk of atherosclerosis.

| Conditions | Rule 1 | Rule 2 | Rule 3 | Rule 4 | Rule 5 |
|------------|--------|--------|--------|--------|--------|
| Cholesterol (mg/dl) | ≤124 | ≤ 124 | 125 – 200 | 125 – 200 | ≥ 201 |
| Blood pressure (mm Hg) | ≤ 140 | > 140 | ≤ 140 | > 140 | – |
| Action |  |  |  |  |  |
| Risk level | very low | low | medium | high | very high |

You designed the test cases with the following test input data:

TC1: Cholesterol = 125 mg/dl Blood pressure = 141 mm Hg  
TC2: Cholesterol = 200 mg/dl Blood pressure = 201 mm Hg  
TC3: Cholesterol = 124 mg/dl Blood pressure = 201 mm Hg  
TC4: Cholesterol = 109 mg/dl Blood pressure = 200 mm Hg  
TC5: Cholesterol = 201 mg/dl Blood pressure = 140 mm Hg  

What is the decision table coverage achieved by these test cases?

## answers
a) 40%  
b) 60%  
c) 80%  
d) 100%  

## justification
There are five columns in the decision table. Each test case covers one of them.  
TC1 and TC2 both cover Rule 4  
TC3 and TC4 both cover Rule 2  
TC5 covers Rule 5  
So, these five test cases cover three out of five columns, achieving a coverage of (3/5)*100% = 60%. Therefore, option b) is the CORRECT option.  

a) Is not correct  
b) Is correct  
c) Is not correct  
d) Is not correct  

# metadata
lo: 4.2.4
k-level: K3
points: 1
correct: c

## question
A storage system can store up to three elements and is modeled by the following state transition diagram. The variable N represents the number of currently stored elements. 

![question-b-23](exam-b-q23.png){width=13cm}

Which of the following test cases, represented as sequences of events, achieves the highest level of valid transitions coverage?

## answers
a) Add, Remove, Add, Add, Add  
b) Add, Add, Add, Add, Remove, Remove  
c) Add, Add, Add, Remove, Remove  
d) Add, Add, Add, Remove, Add  

## justification
Let us refer to the transitions with E1, …, E5 as in the picture. The variable N denotes the number of elements currently stored. Each “Add” event increases it by 1, and each “Remove” event decreases it by 1. Notice, that when the “Add” event occurs while being in the NOT FULL state, the state changes to FULL only if N=2. If N<2, the system stays in the NOT FULL state. If N=0, no “Remove” action is possible. Similarly, if N=3, no “Add” action is possible. Test a) can be written as E1, E3, E3, E2, E4 (so covers 4 out of 5 valid transitions, achieving 80% valid transitions coverage). Test b) is infeasible, because after the first three “Add” actions the system is in the FULL state and there is no valid transition going from FULL triggered by the “Add” event. After the first three transitions only 60% of valid transitions coverage is achieved. Test c) can be written as E1, E2, E4, E5, E3 (so covers 5 out of 5 valid transitions, achieving 100% valid transitions coverage). Test d) can be written as E1, E2, E4, E5, E4 (so covers 4 out of 5 valid transitions, achieving 80% valid transitions coverage).

a) Is not correct  
b) Is not correct  
c) Is correct  
d) Is not correct  

# metadata
lo: 4.3.1
k-level: K2
points: 1
correct: b

## question
You run two test cases, T1 and T2, on the same code. Test T1 achieved 40% statement coverage and test T2 achieved 65% statement coverage. Which of the following sentences must be necessarily true?

## answers
a) The test suite composed with tests T1 and T2 achieves 105% statement coverage  
b) There exists at least one statement that must have been executed by both T1 and T2  
c) At least 5% of the statements in the code under test are non-executable  
d) The test suite composed of tests T1 and T2 achieves full branch coverage  

## justification
a) Is not correct. Coverage is always defined as the percentage of the covered elements. Therefore, it cannot exceed 100%  
b) Is correct. If the statements executed by T1 and T2 were disjoint, the coverage of the test suite {T1, T2} would be 105%, which is impossible (see answer a). Therefore, at least 5% of executable statements must have been executed by both T1 and T2  
c) Is not correct. Statement coverage does not tell us anything about the number of non-executable statements in the code  
d) Is not correct. Even if a test suite achieves full statement coverage, this does not imply achieving full branch coverage  

# metadata
lo: 4.3.2
k-level: K2
points: 1
correct: c

## question
Let the branch coverage metric be defined as BCov = (X / Y) * 100%. What do X and Y represent in this formula?

## answers
a) X = number of decision outcomes exercised by the test cases, Y = total number of decision outcomes in the code  
b) X = number of conditional branches exercised by the test cases, Y = total number of branches in the code  
c) X = number of branches exercised by the test cases, Y = total number of branches in the code  
d) X = number of conditional branches exercised by the test cases, Y = total number of decision outcomes in the code  

## justification
Branch testing is a white-box test technique in which the coverage items are branches. A branch is a transfer of control between two nodes in the control flow graph, which shows the possible sequences in which source code statements are executed in the test object. Each transfer of control can be either unconditional (i.e., straight-line code) or conditional (i.e., a decision outcome). Coverage is measured as the number of branches exercised by the test cases divided by the total number of branches, and is expressed as a percentage.

a) Is not correct. A decision outcome is a conditional branch. For branch testing, X counts not only conditional, but also unconditional branches  
b) Is not correct. Branch coverage counts not only conditional, but also unconditional branches  
c) Is correct. Branch coverage is measured as the number of branches exercised by the test cases divided by the total number of branches, and is expressed as a percentage  
d) Is not correct. Both X and Y count only conditional branches and do not take into account the unconditional branches  

# metadata
lo: 4.4.2
k-level: K2
points: 1
correct: a,e

## question
Which TWO of the following statements provide the BEST rationale for using exploratory testing?

## answers
a) Testers have not been allocated enough time for test design and test execution  
b) The existing test strategy requires that testers use formal, black-box test techniques  
c) The specification is written in a formal language that can be processed by a tool  
d) Testers are the members of an agile team and have good programming skills  
e) Testers are experienced in the business domain and have good analytical skills  

## justification
Exploratory testing is useful when there are few or inadequate specifications or there is significant time pressure on the testing. Exploratory testing is also useful to complement other more formal test techniques. Exploratory testing will be more effective if the tester is experienced, has domain knowledge and has a high degree of essential skills, like analytical skills, curiosity and creativeness

a) Is correct. Exploratory testing is useful when there are few or inadequate specifications or there is significant time pressure on the testing  
b) Is not correct. Exploratory testing is not a black-box test technique  
c) Is not correct. Exploratory testing is useful when the specifications are poorly written  
d) Is not correct. Programming skills have nothing to do with exploratory testing in principle  
e) Is correct. Exploratory testing will be more effective if the tester is experienced, has domain knowledge and has a high degree of essential skills, like analytical skills, curiosity and creativeness  

# metadata
lo: 4.4.3
k-level: K2
points: 1
correct: d

## question
Which of the following BEST fits as an element of the checklist used in checklist-based testing?

## answers
a) “The developer made an error when implementing the code”  
b) “The achieved statement coverage exceeds 85%”  
c) “The program works correctly regarding functional and non-functional requirements”  
d) “The error messages are written in language that the user can understand”  

## justification
a) Is not correct. Checklists should contain test conditions to be verified. This is an example of an error, not a test condition; even if the tester was able to deduce some potential test conditions from the examples of errors, this error description is too general  
b) Is not correct. Checklists should not contain items that are better suited as exit criteria. This is an example of an exit criterion  
c) Is not correct. Checklists should not contain items that are too general. This is a very general item, which practically describes the goal of testing  
d) Is correct. This is an example of a test condition that can be checked by a human  

# metadata
lo: 4.5.2
k-level: K2
points: 1
correct: b

## question
Consider the following acceptance criteria for a user story written from the perspective of an online store owner

```
Given that the user is logged in and on the homepage,  
When the user clicks on the "Add Item" button,  
Then the "Create Item" form should appear,  
And the user should be able to input a name and price for the new item.
```

In what format is this acceptance criteria written?

## answers
a) Rule-oriented  
b) Scenario-oriented  
c) Product-oriented  
d) Process-oriented  

## justification
a) Is not correct. The rule-oriented format includes formats like bullet point verification lists or tabulated forms of input-output mappings, explicitly showing the rules to be followed. Given/When/Then is a scenariooriented format because it describes a scenario to be verified  
b) Is correct. This is a Given/When/Then format, which is scenario-oriented  
c) Is not correct. There no "product-oriented" format of acceptance criteria  
d) Is not correct. There is no "process-oriented" format of acceptance criteria  

# metadata
lo: 4.5.3
k-level: K3
points: 1
correct: d

## question
Your team analyzes the following user story in order to define the acceptance criteria:

```
As a registered customer, I want to be able to view my previous orders on the company's website, so that I can keep track of my purchases.
```

Which of the following test cases will NOT be relevant for this user story?

## answers
a) Input: the customer logs into their account on the website and clicks the “see order history” button, Expected output: the system shows a list of all the customer’s previous orders, including the date, order number, and total cost  
b) Input: the customer clicks on an order from the order list, Expected output: the system displays the individual items purchased, along with their prices and quantities  
c) Input: the customer clicks “Sort ascending” button on the order history screen, Expected output: the system shows the order history sorted by order number in ascending order  
d) Input: an unregistered customer registers as a new customer with a valid e-mail address, that does not already exist in the customer database, Expected output: the system accepts the registration and creates the account  

## justification
a) Is not correct. The test case is related to viewing previous orders in the order history  
b) Is not correct. The test case is related to viewing previous orders  
c) Is not correct. The test case is related to viewing previous orders in the order history  
d) Is correct. The test case is related to the registration process, which is not discussed in the user story. The user story is about viewing previous orders  

# metadata
lo: 5.1.3
k-level: K2
points: 1
correct: a

## question
Your team follows the process that uses the DevOps delivery pipeline. The first three steps of this process are:

(1) Code development  
(2) Submit code into a version control system and merge it into the “test” branch  
(3) Perform component testing for the submitted code  

Which of the following is BEST suited to be the entry criterion for step (2) of this pipeline?

## answers
a) Static analysis returns no high severity warnings for the submitted code  
b) System version control reports no conflicts when merging code into the “test” branch  
c) Component tests are compiled and ready to be executed  
d) Statement coverage is at least 80%  

## justification
a) Is correct. This is something that can (and should) be checked before the code is submitted to version control  
b) Is not correct. This is something that can be checked after step (2) is performed, because merge conflict reporting can be done after the code is submitted and merged  
c) Is not correct. This fits better as the entry criterion for step (3)  
d) Is not correct. This fits better as the exit criterion for step (3)  

# metadata
lo: 5.1.4
k-level: K3
points: 1
correct: b

## question
You want to estimate the test effort for the new project using estimation based on ratios. You calculate the test-to-development effort ratio using averaged data for both development effort and test effort from four historical projects similar to the new one. The table shows this historical data. 

| Project | Development effort ($) | Test effort ($) |
|---------|------------------------|-----------------|
| P1 | 800,000 | 40,000 |
| P2 | 1,200,000 | 130,000 |
| P3 | 600,000 | 70,000 |
| P4 | 1,000,000 | 120,000 |

The estimated development effort for the new project is $800,000. What is your estimate of the test effort in this project?

## answers
a) $40,000  
b) $80,000  
c) $81,250  
d) $82,500  

## justification
The average development effort is $900,000 and the average test effort is $90,000 (calculated from the four projects). The average test-to-development effort ratio is 1:10 ($90,000 : $900,000), which means that historically, on average, the test effort is 10% of the development effort. So if the development effort is estimated to be $800,000, the estimated test effort is estimated as:
10% * $800,000 = 0.1 * $800,000 = $80,000.

a) Is not correct  
b) Is correct  
c) Is not correct  
d) Is not correct  

# metadata
lo: 5.1.5
k-level: K3
points: 1
correct: a

## question
You are testing a web application that allows users to SEARCH for products, VIEW product details, ADD products to a shopping cart, and place an ORDER. You have prepared the following five test cases, which you want to execute according to their priorities:  

TC1: SEARCH product A                 Priority: medium  
TC2: VIEW product A details           Priority: low  
TC3: ADD product B to a shopping cart Priority: medium  
TC4: ADD product C to a shopping cart Priority: high  
TC5: place an ORDER                   Priority: high

You also identified the following logical dependencies between test cases:

* SEARCH functionality must be tested before VIEW functionality can be tested, as product details rely on search functionality.
* VIEW functionality must be tested before ADD functionality, as adding products relies on the availability of accurate product details.
* ADD functionality must be tested before ORDER functionality, as placing an order relies on the availability of accurate shopping cart information.

Which test case should be executed as the fourth one? 

## answers
a) TC3  
b) TC1  
c) TC2  
d) TC4  

## justification
According to the dependencies, SEARCH tests must be executed first, then VIEW tests, then ADD tests and, at the end, ORDER tests. Within each of these groups the order is determined by the priorities of the test cases. So, TC1 must be executed first, then TC2, then TC4 followed by TC3, and then TC5 as the last one. So, the ordering is: TC1, TC2, TC4, TC3, TC5. 

a) Is correct. TC3 will be the fourth test case executed  
b) Is not correct  
c) Is not correct  
d) Is not correct  

# metadata
lo: 5.1.7
k-level: K2
points: 1
correct: d

## question
According to the testing quadrants model, which of the following falls into quadrant Q1 (“technology facing” and “support the team”)?

## answers
a) Usability testing  
b) Functional testing  
c) User acceptance testing  
d) Component integration testing  

## justification
a) Is not correct. Usability testing is business facing testing that critiques the product (Q3)  
b) Is not correct. Functional testing is business facing testing (Q2)  
c) Is not correct. User acceptance testing is business facing testing that critiques the product (Q3)  
d) Is correct. Component integration testing is technology facing testing that supports the team (guides the development) (Q1)  

# metadata
lo: 5.2.4
k-level: K2
points: 1
correct: c

## question
Given the following risks:

1. Ineffective loop implementation causes long system responses
2. Consumers change their preferences
3. Flooding of the server room
4. Patients above a certain age receive inaccurate reports

And the following mitigation activities:

A. Risk acceptance
B. Performance testing
C. Using boundary value analysis as the test technique
D. Risk transfer
 
Which of the following BEST matches the risks with the mitigation activities?

## answers
a) 1C, 2D, 3A, 4B  
b) 1B, 2D, 3A, 4C  
c) 1B, 2A, 3D, 4C  
d) 1C, 2A, 3D, 4B  

## justification
Considering each of the listed risks and their mitigations:

1. Long system responses (1) can be tested in performance testing (B)
2. Changes of consumers’ preferences (2) are usually out of our control, so usually we accept this risk (A)
3. Flooding of the server room (3) can cause significant loss, so we should transfer the risk, e.g., by buying an insurance policy (D)
4. That patients above a certain age receive inaccurate reports (4) suggests a potential boundary problem, which can be effectively detected with techniques like BVA (C)

a) Is not correct  
b) Is not correct  
c) Is correct. The correct combinations of risk and mitigation are: 1B, 2A, 3D and 4C  
d) Is not correct  

# metadata
lo: 5.3.1
k-level: K1
points: 1
correct: a

## question
Which of the following is a product quality metric?

## answers
a) Mean time to failure  
b) Number of defects found  
c) Requirements coverage  
d) Defect detection percentage  

## justification
a) Is correct. Product quality metrics measure quality characteristics. Mean time to failure measures maturity, so it is a product quality metric  
b) Is not correct. This is an example of a defect metric, not a product quality metric  
c) Is not correct. This is an example of a coverage metric, not a product quality metric  
d) Is not correct. This is an example of a defect metric, not a product quality metric  

# metadata
lo: 5.3.3
k-level: K2
points: 1
correct: a

## question
You are a member of a test team located in North America, developing a product for a client located in Europe. The team is agile and follows the DevOps approach and uses a continuous integration/continuous delivery pipeline. Which of the following is the LEAST effective way to communicate test progress to the customer?

## answers
a) Face-to-face  
b) Dashboards  
c) Email  
d) Video conferencing  

## justification
a) Is correct. The client is in a different location and time zone, so it may be difficult to communicate face-to-face  
b) Is not correct. Dashboards are usually available to any user at any time, so the difference in time zones will not be as much of a hindrance to communication as verbal, face-to-face communication  
c) Is not correct. Although the time difference between Europe and America is several hours, and this may cause some inconvenience, it's certainly not as great as with communicating face-to-face  
d) Is not correct. Video conferencing tools are a convenient means of communication. Although communication between Europe and America during working hours usually requires one party to connect in the very early or very late hours, this is not as much of an inconvenience as verbal, face-to-face communication  

# metadata
lo: 5.4.1
k-level: K2
points: 1
correct: a

## question
Which of the following BEST describes an example of how configuration management (CM) supports testing?

## answers
a) Having the version number of the environment, the CM tool can retrieve the version numbers of libraries, stubs and drivers used in that environment  
b) Having a record of the values of the test inputs, the CM tool can execute the test cases for these configurations and calculate test coverage  
c) Having data about the date of purchase of a software license, the CM tool automatically generates information about the fact that the product license is coming to an end  
d) Having the version number of the test case, the CM tool can automatically generate test data for this test case  

## justification
a) Is correct. For a complex configuration item (e.g., a test environment), CM records the items it consists of, their relationships, and versions  
b) Is not correct. CM tools do not execute test cases and do not calculate coverage  
c) Is not correct. A CM tool is not a license management tool  
d) Is not correct. CM tools do not generate test data  

# metadata
lo: 5.5.1
k-level: K3
points: 1
correct: b

## question
You are testing a sort function that gets a set of numbers as input and returns the same set of numbers sorted in ascending order. The log from the test execution looks as follows.

```
Environment configuration: sort function build 2.002.2182, test case set: TCS-3, # of TCs: 5
Test run ID: 736
Start 12:43:21.003
12:43:21.003 Execution of TC1. Input: 3. Output: 3. Result: passed
12:43:21.003 Execution of TC2. Input: 3 11 6 5. Output: 3 5 6 11. Result: passed
12:43:21.004 Execution of TC3. Input: 8 7 3 7 1. Output: 1 3 7 8. Result: failed
12:43:21.005 Execution of TC4. Input: -2 -2 -2 -3 -3. Output: -3 -2. Result: failed
12:43:21.005 Execution of TC5. Input: 0 -2 0 3 4 4. Output: -2 0 3 4. Result: failed
End 12:43:21.005
Total time of test cycle: 0:00:00.002
```

Which of the following provides the BEST description of the failure that can be used in a defect report?

## answers
a) The system fails to sort several sets of numbers. Reference: TC3, TC4, TC5.  
b) The system seems to disregard duplicates while sorting. Reference: TC3, TC4, TC5.  
c) The system fails to sort negative numbers. Reference: TC4, TC5.  
d) TC3, TC4 and TC5 have defects (duplicate input data) and should be corrected.  

## justification
a) Is not correct. While the sentence is true, it does not provide much value for the developer  
b) Is correct. From the test results it seems that the system ignores duplicates and sorts the list disregarding the repetitions. This is probably the cause of failures in TC3, TC4, TC5. Such information may help the developer to find the defect and fix it more efficiently  
c) Is not correct. The system does not fail in sorting negative numbers. The problem is rather in disregarding duplicates  
d) Is not correct. The test cases TC3, TC4 and TC5 fail, but we aren’t aware that the test cases have any defects  

# metadata
lo: 6.1.1
k-level: K2
points: 1
correct: c

## question
Given the following descriptions:

1. Support workflow tracking 
2. Facilitate communication
3. Virtual machines
4. Support reviews

And the following test tool categories:

A. Static testing tools 
B. Tools supporting scalability and deployment standardization
C. DevOps tools
D. Collaboration tools 

Which of the following BEST matches the the descriptions and categories?  

## answers
a) 1A, 2B, 3C, 4D  
b) 1B, 2D, 3C, 4A  
c) 1C, 2D, 3B, 4A  
d) 1D, 2C, 3A, 4B  

## justification
Considering each of the listed tool categories and their descriptions:

A. Static testing tools – support the tester in performing reviews and static analysis (4)
B. Tools supporting scalability and deployment standardization – For example, virtual machines, containerization tools (3)
C. DevOps tools – support the DevOps delivery pipeline, workflow tracking, automated build process(es), continuous integration/continuous delivery (CI/CD) (1)
D. Collaboration tools – facilitate communication (2)

a) Is not correct  
b) Is not correct  
c) Is correct. The correct match is: 1C, 2D, 3B, 4A  
d) Is not correct  

# metadata
lo: 6.2.1
k-level: K1
points: 1
correct: a

## question
Which of the following is MOST likely to be a benefit of test automation?

## answers
a) It provides coverage measures that are too complicated for humans to derive  
b) It shares responsibility for the testing with the tool vendor  
c) It removes the need for critical thinking when analyzing test results  
d) It generates test cases from an analysis of the program code  

## justification
a) Is correct. Test automation can provide measures that are too complicated for humans to derive, such as white-box test coverage measures for all but the most trivial code  
b) Is not correct. By using test tools the responsibility for the testing is NOT shared with the tool vendor as the vendor is not involved in the testing, and it is the tester’s responsibility. The only possible responsibility that could be assigned to the tool vendor is if the tool fails to work as expected and provides incorrect test results  
c) Is not correct. Testers still need to perform critical thinking when analyzing anomalies in the test results to determine their likely cause  
d) Is not correct. Neither testers nor tools can generate test cases simply from an analysis of the program code as the code is the implementation and provides no information on the expected results, which will need to come from another part of the test basis, such as the design specification  
