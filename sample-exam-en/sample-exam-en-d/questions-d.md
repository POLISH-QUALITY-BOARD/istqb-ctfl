# metadata
lo: 1.1.1
k-level: K1
points: 1
correct: d

## question
Which of the following is a typical test objective?

## answers
a) Finding and fixing defects in the test object  
b) Maintaining effective communications with developers  
c) Validating that legal requirements have been met  
d) Building confidence in the quality of the test object  

## justification
a) Is not correct. Finding and fixing defects in the test object is not a typical test objective as although identifying defects is an objective of testing, fixing defects is not a testing activity  
b) Is not correct. Maintaining effective communications with developers is not a typical test objective as although it is useful in achieving other objectives of testing, such as providing stakeholders with information that enables them to make informed decisions, it is not a primary reason for performing testing  
c) Is not correct. Validating that legal requirements have been met is not a typical test objective because validation is concerned with checking whether the system meets users’ and other stakeholders’ needs in its operational environment. Checking that legal requirements have been met is a form of verification  
d) Is correct. Building confidence in the quality of the test object is achieved by executing tests that pass  

# metadata
lo: 1.2.3
k-level: K2
points: 1
correct: c

## question
A designer documents a design for a user interface that does not suitably address disabled users because the designer is tired. The programmer implements the user interface in line with the design but as they are working under severe time pressure, they do not include suitable exception handling in their program code for bonus calculations. When the operational system is used, complaints are made by some disabled users about the interface and the company is subsequently fined by the relevant regulatory authority. No one notices that bonus calculations are sometimes incorrect. Which of the following statements is CORRECT?

## answers
a) The miscalculation of bonuses is a defect that occasionally occurs  
b) The fine received for failing to address some disabled users is a failure  
c) The programmer working under severe time pressure is a root cause  
d) The design of the user interface includes a designer error  

## justification
a) Is not correct. The miscalculation of bonuses is a failure by the system, not a defec  
b) Is not correct. The system not suitably supporting disabled users is a failure which eventually results in a fine, but the fine itself is not a failure (it appears to be the correct functioning of the regulatory system)  
c) Is correct. The error is made by the programmer and this mistake is caused by them working under severe time pressure, which is the root cause of the subsequent defect  
d) Is not correct. The poor design of the user interface, which does not suitably address disabled users, is a design defect caused by the designer error. Thus the design of the user interface includes a design defect not a designer error  

# metadata
lo: 1.3.1
k-level: K2
points: 1
correct: a

## question
High-level test conditions are being used by testers to generate test cases and execute tests. Even though the test conditions remain the same, the test cases are varied each time. Which of the following ‘principles of testing’ is being addressed through the variation of test cases?

## answers
a) Tests wear out  
b) Absence-of-defects fallacy  
c) Early testing saves time and money  
d) Defects cluster together  

## justification
a) Is correct. The ‘tests wear out’ principle is concerned with the idea that repeating identical tests on unaltered code is unlikely to uncover novel defects and therefore, modifying tests may be essential. By using highlevel test conditions to generate new tests each time, the tests will not be identical and should not ‘wear out’  
b) Is not correct. The ‘absence-of-defects fallacy’ principle is concerned with ensuring that users’ needs are fulfilled even if lots of testing is done and no defects are found (i.e., validation is also necessary). The use of high-level test conditions to generate test cases and execute tests does not directly address this concern  
c) Is not correct. The ‘early testing saves time and money’ principle is concerned with fixing defects early on to prevent the occurrence of subsequent defects in derived work products, thereby reducing costs and the likelihood of failures. This is typically addressed by starting testing (both static and dynamic) as early as possible, but this is not addressed by using high-level test conditions to generate test cases and execute tests  
d) Is not correct. The ‘Defects cluster together’ principle is concerned with the distribution of defects in a system, which typically follows a Pareto distribution. The use of high-level test conditions to generate test cases and execute tests does not address this concern, which is typically addressed by risk-based testing  

# metadata
lo: 1.4.1
k-level: K2
points: 1
correct: b

## question
Given the following test tasks:

1. Derive test cases from test conditions
2. Identify reusable testware
3. Organize test cases into test procedures
4. Evaluate test basis and test object

And the following test activities:

A. Test analysis
B. Test design
C. Test implementation
D. Test completion

Which of the following BEST matches the tasks with the activities?

## answers
a) 1B, 2A, 3D, 4C  
b) 1B, 2D, 3C, 4A  
c) 1C, 2A, 3B, 4D  
d) 1C, 2D, 3A, 4B  

## justification
a) Is not correct  
b) Is correct. The CORRECT match is: 1B, 2D, 3C, 4A  
c) Is not correct  
d) Is not correct  

# metadata
lo: 1.4.3
k-level: K2
points: 1
correct: a

## question
Given the following testware:

i. Test completion report
ii. Data held in a database used for test inputs and expected results
iii. The list of elements needed to build the test environment
iv. Documented sequences of test cases in execution order
v. Test cases

Which of the following BEST shows the testware produced as a result of performing test implementation?

## answers
a) ii, iv  
b) iii, v  
c) i, ii, v  
d) i, iii, iv  

## justification
a) Is correct. Items ii and iv in the list are produced as a result of test implementation  
b) Is not correct  
c) Is not correct  
d) Is not correct  

# metadata
lo: 1.4.5
k-level: K2
points: 1
correct: d

## question
Which of the following is MOST likely to describe a task performed by someone in a test management role?

## answers
a) Evaluate test basis and test object  
b) Define test environment requirements  
c) Assess testability of test object  
d) Create test completion report  

## justification
a) Is not correct. The testing role is primarily responsible for the technical and engineering aspects of testing, such as test analysis, test design, test implementation, and test execution. Evaluating the test basis for defects and the test object for testability are tasks performed as part of test analysis, so it is likely they are tasks performed by the testing role  
b) Is not correct. The testing role is primarily responsible for the technical and engineering aspects of testing, such as test analysis, test design, test implementation, and test execution. Defining the test environment requirements is a task performed as part of test design, so it is likely to be a task performed by the testing role  
c) Is not correct. The testing role is primarily responsible for the technical and engineering aspects of testing, such as test analysis, test design, test implementation, and test execution. Assessing the testability of a test object is a task performed as part of test analysis, so it is likely to be a task performed by the testing role  
d) Is correct. The test management role primarily involves activities related to test planning, test monitoring and control, and test completion. Thus, creating the test completion report, which is the prime output from the test completion activity, is likely to be a task performed by the test management role  

# metadata
lo: 1.5.2
k-level: K1
points: 1
correct: a

## question
Which of the following is an advantage of the whole team approach?

## answers
a) Improved communication between team members  
b) Decreased individual accountability for quality  
c) Faster deployment of deliverables to the end users  
d) Reduced collaboration with external business users  

## justification
a) Is correct. The whole team approach promotes robust communication and collaboration between the team members  
b) Is not correct. While the whole team approach prioritizes collective accountability for quality, each individual team member is still equally accountable for quality  
c) Is not correct. The whole team approach is about how the team works together, with the aim of higher quality deliverables, but it does not necessarily result in faster deployment to end users  
d) Is not correct. When using the whole team approach, testers work with business representatives to create acceptance tests. There is no suggestion that the approach will reduce collaboration with external business users  

# metadata
lo: 1.5.3
k-level: K2
points: 1
correct: b

## question
Given the following benefits and drawbacks of the independence of testing:

i. The testers work in a different location from the developers
ii. Testers question the assumptions programmers make while writing code
iii. A confrontational dynamic has been established between testers and developers
iv. Developers have convinced themselves that testers are mostly accountable for quality
v. Testers have different biases than those held by the developers

Which are MOST likely to be considered benefits?

## answers
a) i, iv  
b) ii, v  
c) i, iii, iv  
d) ii, iii, v  

## justification
a) Is not correct  
b) Is correct. The list entries showing benefits are ii and v  
c) Is not correct  
d) Is not correct  

# metadata
lo: 2.1.2
k-level: K1
points: 1
correct: a

## question
Which of the following is a good testing practice that applies to all software development lifecycles?

## answers
a) Each test level has specific and distinct test objectives  
b) Test implementation and execution for a given test level should start during the corresponding development phase  
c) Testers should start test design as soon as drafts of the relevant work products become available  
d) Every dynamic testing activity has a corresponding static testing activity  

## justification
a) Is correct. Each test level has specific and distinct test objectives as a different form of test object (e.g., single component, complete system) is tested at each test level and overlapping test objectives would lead to unnecessary duplication  
b) Is not correct. Test analysis and design for a given test level should start during the corresponding development phase to facilitate early testing (e.g., acceptance test analysis and design should begin during requirements analysis). Test implementation will generally start later, and test execution will start during the test level  
c) Is not correct. Test design for a given test level should start during the corresponding development phase to facilitate early testing, however test design (e.g., test case generation) needs to be based on an agreed test basis, not an early draft, otherwise significant test effort may be wasted on creating test cases for a design that later changes  
d) Is not correct. Quality control applies to all development activities, meaning that every software development activity has a corresponding test activity. However, the same symmetry does not apply to dynamic and static testing. There are some static testing activities (e.g., static analysis) for which there is no obvious corresponding dynamic testing activity  

# metadata
lo: 2.1.3
k-level: K1
points: 1
correct: a

## question
Which of the following is an example of a test-first approach to development?

## answers
a) Behavior-Driven Development  
b) Test Level Driven Development  
c) Function-Driven Development  
d) Performance-Driven Development  

## justification
a) Is correct. Behavior-Driven Development (BDD) is a well-known example of a test-first approach to development  
b) Is not correct. Test Level Driven Development is not a correct example of a test-first approach to development  
c) Is not correct. Function-Driven Development is not a correct example of a test-first approach to development  
d) Is not correct. Performance-Driven Development is not a correct example of a test-first approach to development  

# metadata
lo: 2.1.4
k-level: K2
points: 1
correct: d

## question
Which of the following is MOST likely to be a challenge encountered when implementing DevOps?

## answers
a) Making sure that non-functional quality characteristics are not overlooked  
b) Managing continuously changing test environments  
c) The need for more manual testers with suitable experience  
d) Setting up the test automation as part of the delivery pipeline  

## justification
a) Is not correct. DevOps generally increases the visibility of non-functional quality characteristics, such as performance and reliability  
b) Is not correct. Automated processes like continuous integration/continuous delivery (CI/CD) used in DevOps facilitate stable test environments  
c) Is not correct. Automated processes like CI/CD used in DevOps generally reduce the need for manual testing  
d) Is correct. DevOps implementation can pose several risks and challenges, including the need to define and set up the delivery pipeline, introduce and maintain CI/CD tools, and establish and maintain test automation  

# metadata
lo: 2.1.6
k-level: K2
points: 1
correct: b

## question
Which of the following BEST describes retrospectives?

## answers
a) Retrospectives allow team members to identify other team members who did not fully contribute to achieving quality as required by the whole-team approach  
b) Retrospectives give testers an opportunity to identify activities that were successful so that these are retained when potential improvements are made in the future  
c) Retrospectives are where agile team members are allowed to voice their concerns about management and customers in a blame-free environment  
d) Retrospectives give agile team members a forum where they focus on discussing the plan and technical decisions for the next iteration  

## justification
a) Is not correct. The benefits of retrospectives include team bonding and learning from sharing issues, and better collaboration between developers and testers through reviewing and improving working practices. Calling out individuals who a team member may feel did not fully contribute to achieving quality as required by the whole-team approach will not contribute to this team bonding and collaboration  
b) Is correct. During the retrospective, the group discusses what aspects of the project were successful and should be retained, as well as areas that could be improved, and how to do so  
c) Is not correct. The benefits of retrospectives are based on increased effectiveness and efficiency through process improvements; they are not an opportunity to let off steam and criticize management and customers. Also, the results are recorded, usually in the test completion report, so anything said in the meeting could be read by other stakeholders  
d) Is not correct. Retrospectives are meetings that are typically held at the end of an iteration where team members will focus on discussing quality-related issues that have occurred in the current iteration. They are not used for making plans or technical decisions for the next iteration; this would be done in the iteration planning meeting at the start of the next iteration  

# metadata
lo: 2.2.2
k-level: K2
points: 1
correct: a

## question
Which of the following tests is MOST likely to be performed as part of functional testing?

## answers
a) The test checks that the sort function puts the elements of the list or array in ascending order  
b) The test checks whether the sort function completes sorting within one second of starting  
c) The test checks how easily the sort function can be changed from sorting ascending to sorting descending  
d) The test checks that the sort function still functions correctly when moved from a 32-bit to a 64-bit architecture  

## justification
a) Is correct. Checking that the sort function puts the elements of the list or array in ascending order is evaluating the functional correctness of the sort function, which is part of functional testing  
b) Is not correct. Assessing whether the sort function meets its nonfunctional requirement to complete within one second is part of testing its performance efficiency, which is part of non-functional testing  
c) Is not correct. Evaluating the ease with which the sort function can be modified from sorting ascending to sorting descending is testing its modifiability, a form of non-functional maintainability testing, which is part of non-functional testing  
d) Is not correct. Assessing that the sort function still functions correctly when moved from a 32-bit to a 64-bit architecture is testing its adaptability, a form of portability testing, which is part of non-functional testing  

# metadata
lo: 2.3.1
k-level: K2
points: 1
correct: b

## question
Which of the following is MOST likely to be a trigger that leads to maintenance testing of a currency exchange system?

## answers
a) The developers reported that changing the currency exchange system was difficult and the testers decided to check if this was true  
b) The refund option of the currency exchange system was removed as it did not always repay the correct amount to customers  
c) The agile team has started developing a user story that adds a new customer loyalty feature to the currency exchange system  
d) The currency exchange system was reconfigured to support both English and local language currency transactions  

## justification
a) Is not correct. Assuming that testers could check the ease of changing the currency exchange system then it would be done by maintainability testing rather than maintenance testing, so this is not a trigger for maintenance testing  
b) Is correct. A system modification (such as a fix or enhancement) is an example of a trigger for maintenance testing. The removal of the refund option of the currency exchange system was a fix that would lead to maintenance testing  
c) Is not correct. If the agile team has started developing a user story that adds a new customer loyalty feature to the currency exchange system, then this will result in them testing the new feature, and then they would perform regression testing. No maintenance testing is required in this situation  
d) Is not correct. Reconfiguration of the currency exchange system to support both the local language and English currency transactions is not a system modification, a change to the operational environment, or a system retirement, which are the three triggers for maintenance testing  

# metadata
lo: 3.1.1
k-level: K1
points: 1
correct: c

## question
Which of the following CANNOT be examined by static testing?

## answers
a) Contract  
b) Test plan  
c) Encrypted code  
d) Test charter  

## justification
a) Is not correct. Most work products can be examined using some form of static testing, and a contract must be interpretable by humans and so could be reviewed, which is a form of static testing  
b) Is not correct. Most work products can be examined using some form of static testing, and a test plan must be interpretable by humans and so could be reviewed, which is a form of static testing  
c) Is correct. Most work products can be examined using some form of static testing; however it is not suitable for work products that are too complex for human interpretation and should not be analyzed by tools, and encrypted code is too complex for humans and if it is properly encrypted it will not be analyzable by most tools  
d) Is not correct. Most work products can be examined using some form of static testing, and a test charter must be interpretable by humans and so could be reviewed, which is a form of static testing  

# metadata
lo: 3.1.2
k-level: K2
points: 1
correct: c

## question
Which of the following statements about the value of static testing is CORRECT?

## answers
a) The defect types found by static testing are different from the defect types that can be found by dynamic testing  
b) Dynamic testing can detect the defect types that can be found by static testing plus some additional defect types  
c) Dynamic testing can identify some of the defects that can be found by static testing but not all of them  
d) Static testing can identify the defect types that can be found by dynamic testing as well as some extra defect types  

## justification
a) Is not correct. There are some defect types that can be found by both static testing and dynamic testing, such as a programming defect that can be observed by a reviewer in a code review and which causes an observable failure during dynamic testing  
b) Is not correct. There are some defect types that can only be detected by static testing, such as unreachable code, design patterns not implemented as desired and defects in non-executable work products  
c) Is correct. There are some defect types that can be found by both static testing and dynamic testing, such as a programming defect that can be observed by a reviewer in a code review and which causes an observable failure during dynamic testing. There are also some defect types that can only be detected by static testing, such as unreachable code, design patterns not implemented as desired and defects in nonexecutable work products  
d) Is not correct. There are some defect types that can only be detected by dynamic testing, such as performance issues or memory issues that can only be observed when executing the code or system  

# metadata
lo: 3.2.2
k-level: K2
points: 1
correct: b

## question
Given the following descriptions of review activities:

1. Detected anomalies are deliberated upon, and determinations are reached regarding their status, ownership, and any further steps needed
2. Issues are recorded, and any needed updates are addressed prior to the acceptance of the work product
3. Reviewers employ techniques to come up with suggestions and questions about thework product and to spot anomalies
4. The objective of the review and its schedule are established to ensure a focused and efficient review
5. Participants are provided with access to the item being reviewed

Which of the following is the CORRECT sequence in the review process of the activities that correspond to the descriptions?

## answers
a) 4 – 3 – 5 – 2 – 1  
b) 4 – 5 – 3 – 1 – 2  
c) 5 – 4 – 1 – 3 – 2  
d) 5 – 4 – 3 – 2 – 1  

## justification
a) Is not correct  
b) Is correct. The correct sequence of activities is: 4 – 5 – 3 – 1 – 2  
c) Is not correct  
d) Is not correct  

# metadata
lo: 3.2.3
k-level: K1
points: 1
correct: b

## question
Which participant in the review process is responsible for ensuring that the review meetings run effectively and that everyone at the meetings can voice their opinions freely?

## answers
a) Manager  
b) Moderator  
c) Chairperson  
d) Review Leader  

## justification
a) Is not correct. The manager is responsible for deciding what needs to be reviewed and allocating resources, such as staff and time, for the review  
b) Is correct. The moderator (or facilitator) is responsible for ensuring that the review meetings run effectively, including managing time, mediating discussions, and creating a safe environment where everyone can voice their opinions freely  
c) Is not correct. The chairperson is not a recognized role in reviews  
d) Is not correct. The review leader is responsible for overseeing thereview process, such as selecting the review team members, scheduling review meetings, and ensuring that the review is completed successfully  

# metadata
lo: 4.1.1
k-level: K2
points: 1
correct: b

## question
You perform system testing of an e-commerce web application and are provided with the following requirement:  
REQ 05-017. If the total cost of purchases exceeds $100, the customer gets a 5% discount on subsequent purchases. Otherwise, the customer does not receive a discount.

Which test techniques will be MOST helpful in designing test cases based on this requirement?

## answers
a) White-box test techniques  
b) Black-box test techniques  
c) Experience-based test techniques  
d) Risk-based test techniques  

## justification
a) Is not correct. The document does not refer to the test object’s internal structure but specifies the desired behavior of the test object. Therefore, white-box test techniques will not be helpful in designing test cases  
b) Is correct. The document is a requirement that specifies the desired behavior of the test object. Therefore, the most suitable test techniques in this case are the black-box test techniques (e.g., Boundary Value Analysis or Decision Table Testing)  
c) Is not correct. Although experience-based test techniques can be used to design test cases based on this document, black-box test techniques will be more suitable. The document describes a precise business rule and, in addition, wording like "exceeds $100" suggests the existence of important equivalence partition boundaries that should be tested using black-box test techniques like boundary value analysis  
d) Is not correct. Risk-based test techniques are not a recognized type of test technique  

# metadata
lo: 4.2.1
k-level: K3
points: 1
correct: b,e

## question
The system for selling cinema tickets calculates the discount type based on the client’s birth year (BY) and on the current year (CY) as follows:

Let D be the difference between CY and BY, that is, D = CY – BY

* If D < 0 then print the error message “birth year cannot be greater than current year”
* If 0 ≤ D < 18 then apply the student discount
* If 18 ≤ D < 65 then apply no discount
* If D ≥ 65 then apply the pensioner discount

Your test suite already contains two test cases:

* BY = 1990, CY = 2020, expected result: no discount
* BY = 2030, CY = 2029, expected result: print the error message

Which of the following test data sets should be added to achieve full valid equivalence partitioning coverage for the discount type?

## answers
a) BY = 2001, CY = 2065  
b) BY = 1900, CY = 1965  
c) BY = 1965, CY = 1900  
d) BY = 2011, CY = 2029  
e) BY = 2000, CY = 2000  

## justification
a) Is not correct. CY – BY = 64, so these inputs correspond to the already covered “no discount” partition  
b) Is correct. CY – BY = 65, so these inputs correspond to a partition that is not yet covered (“pensioner discount”)  
c) Is not correct. CY – BY = –65, so these inputs correspond to the already covered “error message” partition  
d) Is not correct. CY – BY = 18, so these inputs correspond to the already covered “no discount” partition  
e) Is correct. CY – BY = 0, so these inputs correspond to a partition that is not yet covered (“student discount”)  

# metadata
lo: 4.2.2
k-level: K3
points: 1
correct: c

## question
You are testing a temperature control system for a horticultural cold storage facility. The system receives the temperature (in full degrees Celsius) as the input. If the temperature is between 0 and 2 degrees inclusive, the system displays the message “temperature OK”. For lower temperatures, the system displays the message "temperature too low" and for higher temperatures it displays the message “temperature too high”.

Using two-value boundary value analysis, which of the following sets of test inputs provides the highest level of boundary value coverage?

## answers
a) –1, 3  
b) 0, 2  
c) –1, 0, 2, 3  
d) –2, 0, 2, 4  

## justification
a) Is not correct  
b) Is not correct  
c) Is correct. The correct option is: –1, 0, 2, 3  
d) Is not correct  

# metadata
lo: 4.2.3
k-level: K3
points: 1
correct: a

## question
You are designing test cases based on the following decision table.

| Conditions | R1 | R2 | R3 | R4 | R5 | R6 | R7 |
|------------|----|----|----|----|----|----|----|
| C1: Age | 0-18 | 19-65 | 19-65 | >65 | 0-18 | 19-65 | >65 |
| C2: Experience | - | 0-4 | >4 | - | - | - | - |
| C3: Registered? | NO | NO | NO | NO | YES | YES | YES |
| Actions |  |  |  |  |  |  |  |
| Category | A | A | B | B | B | D | C |

So far you have designed the following test cases:

* TC1: 19-year-old, unregistered man with no experience; expected result: category A
* TC2: 65-year-old, unregistered woman with 5 years of experience; expected result: category B
* TC3: 66-year-old, registered man with no experience; expected result: category C
* TC4: 65-year-old, registered woman with 4 years of experience; expected result: category D

Which of the following test cases, when added to the existing set of test cases, will increase the decision table coverage?

## answers
a) 66-year-old, unregistered man with no experience; expected result: category B  
b) 55-year-old, unregistered woman with 2 years of experience; expected result: category A  
c) 19-year-old, registered woman with 5 years of experience; expected result: category D  
d) No additional test case can increase the already achieved decision table coverage  

## justification
a) Is correct. The conditions “66-year-old”, “unregistered” and “no experience” match rule R4, which is not covered by the existing test cases, so after adding this test case, the decision table coverage will increase  
b) Is not correct. The conditions “55-year-old”, “unregistered” and “2 years of experience” match rule R2, already covered by TC1. So adding this test case will not increase the coverage  
c) Is not correct. The conditions “19-year-old”, “registered” and “5 years of experience” match rule R6, already covered by TC4. So adding this test case will not increase the coverage  
d) Is not correct. The existing test cases cover only 4 out of 7 columns of the decision table. The coverage can be increased by adding test cases that cover yet uncovered columns, that is, R1, R4 and R5  

# metadata
lo: 4.2.4
k-level: K3
points: 1
correct: b

## question
You are applying state transition testing to the hotel room reservation system modeled by the following state transition table, with 4 states and 5 different events:

| State | Available | NotAvailable | ChangeRoom | Cancel | Pay |
| ----- | --------- | ------------ | ---------- | ------ | --- |
| S1: Requesting | S2 | S3 |  |  |  |
| S2: Confirmed |  |  | S1 | S4 | S4 |
| S3: Waiting list | S2 |  |  | S4 |  |
| S4: End |  |  |  |  |  |

Assuming all test cases start in the ‘Requesting’ state, which of the following test cases, represented as sequences of events, achieves the highest valid transitions coverage?

## answers
a) NotAvailable, Available, ChangeRoom, NotAvailable, Cancel  
b) Available, ChangeRoom, NotAvailable, Available, Pay  
c) Available, ChangeRoom, Available, ChangeRoom, NotAvailable  
d) NotAvailable, Cancel, ChangeRoom, Available, Pay  

## justification
a) Is not correct. This sequence of five events covers 4 different valid transitions (both “NotAvailable” events correspond to the same transition between S1 and S3). This test case covers 4 out of 7 valid transitions  
b) Is correct. This sequence of five events covers 5 different transitions (the first “Available” event corresponds to a transition between S1 and S2, and the second “Available” event corresponds to a transition between S3 and S2, so two different transitions are covered). This test case covers 5 out of 7 valid transitions and achieves the highest valid transitions coverage  
c) Is not correct. This sequence of five events covers 3 different transitions (both “Available” events correspond to the same transition from S1 to S2; both “ChangeRoom” events correspond to the same transition from S2 to S1). This test case covers 3 out of 7 valid transitions  
d) Is not correct. This sequence of five events does not represent a feasible test case, because after “Cancel” the system ends up in the End state and no further valid transitions can be executed  

# metadata
lo: 4.3.1
k-level: K2
points: 1
correct: c

## question
Your test suite S for a program P achieves 100% statement coverage. It consists of three test cases, each of which achieves 50% statement coverage.

Which of the following statements is CORRECT?

## answers
a) Executing S will cause all possible failures in P  
b) S achieves 100% branch coverage for P  
c) Every executable statement in P containing a defect has been run at least once during the execution of S  
d) After removing one test case from S, the remaining two test cases will still achieve 100% statement coverage  

## justification
a) Is not correct. A line with a defect, when executed, does not have to cause a failure. For example, a line x := y / z will cause a failure only when z equals 0  
b) Is not correct. 100% statement coverage does not guarantee 100% branch coverage. For example, a test case with x=0 for the code  
    1. IF (x=0) THEN
    2. A; 
    3. ENDIF 
   achieves 100% statement coverage but does not cover the branch from 1 to 3
c) Is correct. 100% statement coverage means that each executable statement was executed at least once  
d) Is not correct. The removed test case may provide coverage of some statements that are not covered by either of the other two test cases, in which case the remaining two test cases together will not achieve 100% statement coverage  

# metadata
lo: 4.3.3
k-level: K2
points: 1
correct: a

## question
Why does white-box testing facilitate defect detection even when the software specification is vague, outdated or incomplete?

## answers
a) Test cases are designed based on the structure of the test object rather than the specification  
b) For each white-box test technique the coverage can be well-defined and easily measured  
c) White-box test techniques are very well designed to detect omissions in the requirements  
d) White-box test techniques can be used in both static testing and dynamic testing  

## justification
a) Is correct. A fundamental strength that all white-box test techniques share is that the entire software implementation is taken into account during testing, which facilitates defect detection even when the software specification is vague, outdated or incomplete. This means white-box testing can find defects such as an extra feature added to the code (either accidentally or deliberately) that is not supposed to be there, which black-box testing cannot detect  
b) Is not correct. The fact that the coverage can be precisely defined is not the right reason. The achieved level of coverage would have much more impact than the possibility to measure the coverage  
c) Is not correct. If the software does not implement one or more requirements, white-box testing is unlikely to detect the resulting defects of omission  
d) Is not correct. While this is true, this is not the right answer, because there is no connection between the capability to be used in both static testing and dynamic testing and the claim that white-box testing facilitates defect detection with poor specifications  

# metadata
lo: 4.4.1
k-level: K2
points: 1
correct: c

## question
Which of the following is NOT anticipated by the tester while applying error guessing?

## answers
a) The developer misunderstood the formula in the user story for calculating the interest  
b) The developer wrote “FA = A*(1+IR^N)” instead of “FA = A*(1+IR)^N” in the source code  
c) The developer missed the seminar on new compound interest rate legislation  
d) The accuracy of the interest calculated by the system is not precise enough  

## justification
a) Is not correct. This is an example of anticipating the developer’s error  
b) Is not correct. This is an example of anticipating the defect  
c) Is correct. This is an example of a potential root cause of a defect, which is neither an error, defect nor failure, and difficult for the tester to anticipate  
d) Is not correct. This is an example of anticipating a failure, perhaps based on experience of previous systems in this application domain  

# metadata
lo: 4.4.2.
k-level: K2
points: 1
correct: d

## question
Which of the following is true about exploratory testing?

## answers
a) Test cases are designed before the exploratory testing session starts  
b) The tester can perform test execution, but cannot perform test design  
c) Exploratory testing results are good predictors of the number of remaining defects  
d) During exploratory testing the tester may use black-box test techniques  

## justification
a) Is not correct. In exploratory testing, test cases are usually created during the exploratory testing session, alongside test analysis, test implementation and test execution  
b) Is not correct. In exploratory testing, tests are simultaneously designed, executed, and evaluated while the tester learns about the test object  
c) Is not correct. Exploratory testing results depend heavily on the tester’s experience, so even if the results of exploratory testing can be used as a predictor of risk and used to assess whether there will be fewer or more defects, for example, compared to the previous exploratory testing session, they are not a good example of reliable defect prediction models that can predict the number of remaining defects  
d) Is correct. During exploratory testing, the testers can use any techniques that they find useful  

# metadata
lo: 4.5.1
k-level: K2
points: 1
correct: d

## question
Which collaborative user story writing practice enables the team to achieve a collective understanding of what needs to be delivered?

## answers
a) Planning poker, so that a team can achieve consensus on the effort needed to implement a user story  
b) Reviews, so that a team can detect inconsistencies and contradictions in a user story  
c) Iteration planning, so that user stories with the highest business value for a customer can be prioritized for implementation  
d) Conversation, so that team members can understand how the software will be used  

## justification
a) Is not correct. Planning poker can estimate effort for a user story that is already written. It does not help in understanding what should be delivered  
b) b) Is not correct. Reviews are not a collaborative user story writing practice  
c) Is not correct. Iteration planning is a project-related practice, used to plan the work, not to understand what needs to be delivered  
d) Is correct. Conversation explains how the software will be used and often allows the team to define meaningful acceptance criteria, thus obtaining a shared vision of what should be delivered  

# metadata
lo: 4.5.3
k-level: K3
points: 1
correct: a

## question
You have just started designing test cases for the following user story.

```
As a customer, I want to be able to filter search results by price range, so that I can find products within my budget more easily.
Acceptance criteria:
1. The filter should work for all versions of the application from version 3.0 upwards
2. The filter should allow the customer to set a price range with a minimum and a maximum price
3. The search results should update dynamically as the customer adjusts the price range filter
```

In all test cases the precondition is as follows: there are only two products available, products A and B. Product A costs $100 and product B costs $110.

Which of the following is the BEST example of a test case for this user story?

## answers
a) Enter webpage and set filter to show prices between $90 and $100. Expected result: results show product A only. Set maximum price to $110. Expected result: results now include both products A and B  
b) Enter webpage. Expected result: the default minimum and maximum prices are $100 and $110 respectively. Add product C to stock, with price $120. Refresh the client’s webpage. Expected result: the default maximum price changes to $120  
c) Enter webpage and set filter to show prices between $90 and $115. Expected result: results show both products A and B. Change currency from USD to EUR. Expected result: the filter range changes correctly to EUR values, according to the current exchange rate  
d) Enter webpage with three different browsers: Edge, Chrome and Opera. In each browser set filter between $90 and $110. Expected result: results include both products A and B and the results layout is the same in all three browsers  

## justification
a) Is correct. This test case is related to acceptance criteria 2 and 3, because we check if we can set price range (acceptance criterion 2) and if the results update dynamically after adjusting the price range filter (acceptance criterion 3)  
b) Is not correct. This test case is not related to any of the acceptance criteria. It checks if the filter dynamically sets the default minimum and maximum price range, and not that a customer can do it  
c) Is not correct. This test case is not related to any of the acceptance criteria. It checks the currency exchange feature, which is not discussed in this user story  
d) Is not correct. This test case is not related to any of the acceptance criteria. It checks the application’s compatibility with different browsers, which is not discussed in this user story  

# metadata
lo: 5.1.3
k-level: K2
points: 1
correct: b,d

## question
Which of the following BEST define EXIT criteria in a testing project?

## answers
a) The budget is approved  
b) Budget runs out  
c) Test basis is available  
d) Test cases achieved at least 80% statement coverage  
e) All test analysts are ISTQB certified at the Foundation Level  

## justification
a) Is not correct. The approval of the budget is an example of an entry criterion. It would make no sense to approve the budget for some activity that has already been done  
b) b) Is correct. Running out of budget can be viewed as a valid exit criterion  
c) Is not correct. Availability of resources is an example of an entry criterion for testing  
d) Correct. Coverage is a measure of thoroughness, so it is a typical exit criterion  
e) Is not correct. This is an example of an entry criterion, checked before the project starts  

# metadata
lo: 5.1.4
k-level: K3
points: 1
correct: a

## question
The team wants to estimate the time needed for one tester to execute four test cases for a software component. The team has gathered the following measures of the effort used to execute a single test case:

* Best-case scenario: 1 hour
* Worst-case scenario: 8 hours
* Most likely scenario: 3 hours

Given that the three-point estimation technique is being used, what is the final estimate of the time needed to execute all four test cases?

## answers
a) 14 hours  
b) 3.5 hours  
c) 16 hours  
d) 12 hours  

## justification
a) Is correct. In this case, the estimate for executing a single test case is: E = (1h + 4*3h + 8h) / 6 = 3.5 hours. So, the total time needed for the tester to execute 4 test cases is:3.5h * 4 = 14 hours  
b) Is not correct  
c) Is not correct  
d) Is not correct  

# metadata
lo: 5.1.5
k-level: K3
points: 1
correct: b

## question
The table shows the traceability matrix from test cases to requirements. “X” means that a given test case covers the corresponding requirement.

| Req1 | Req2 | Req3 | Req4 | Req5 | Req6 | Req7 |
|------|------|------|------|------|------|------|
| TC1 | X |   | X | X |   |   | X |
| TC2 | X |   |   |   | X |   | X |
| TC3 |   |   |   |   | X | X |   |
| TC4 |   | X |   |   |   |   |   |

You want to prioritize the test cases following the additional coverage prioritization technique.  
You execute all four test cases.

Which test case should be executed as the LAST one?

## answers
a) TC1  
b) TC2  
c) TC3  
d) TC4  

## justification
a) Is not correct  
b) Is correct  
c) Is not correct  
d) Is not correct  

# metadata
lo: 5.1.7
k-level: K2
points: 1
correct: c

## question
How can the testing quadrants be beneficial for testing?

## answers
a) They help in test planning by dividing the test process into four stages, corresponding to the four basic test levels: component, integration, system, and acceptance testing  
b) They help in assessing the high-level coverage (e.g., requirements coverage) based on low-level coverage (e.g., code coverage)  
c) They help non-technical stakeholders to understand the different types of tests and that some test types are more relevant to certain test levels than others  
d) They help agile teams to develop a communication strategy based on classifying people according to four basic psychological types, and on modelling the relations between them  

## justification
a) Is not correct. Testing quadrants have nothing to do with describing the relationships between test levels  
b) Is not correct. Testing quadrants cannot help in assessing any type of coverage  
c) Is correct. Testing quadrants allow managers and other stakeholders to understand the relationships between test types, the activities they support (team support or product critique), and the viewpoint they are focused on (business- or technology-facing)  
d) Is not correct. Testing quadrants is not a psychological model  

# metadata
lo: 5.2.1
k-level: K1
points: 1
correct: b

## question
For a given risk, its risk level is $1,000 and its risk likelihood is estimated as 50%. What is the risk impact?

## answers
a) $500  
b) $2,000  
c) $50,000  
d) $200  

## justification
a) Is not correct  
b) Is correct  
c) Is not correct  
d) Is not correct  

# metadata
lo: 5.2.2
k-level: K2
points: 1
correct: b,e

## question
Which of the following are product risks?

## answers
a) Scope creep  
b) Poor architecture  
c) Cost-cutting  
d) Poor tool support  
e) Response time too long  

## justification
a) Is not correct. Scope creep is an example of a project risk related to technical issues  
b) Is correct. Poor architecture is an example of a product risk since it refers to a product characteristic  
c) Is not correct. Cost-cutting is an example of a project risk, related to organizational issues  
d) Is not correct. Poor tool support is an example of a project risk related to technical issues  
e) Is correct. Response time too long is an example of a product risk since it refers to a product characteristic  

# metadata
lo: 5.3.2
k-level: K2
points: 1
correct: c

## question
Which of the following is NOT a valid purpose for a test report?

## answers
a) Tracking test progress and identifying areas that require further attention  
b) Providing information on the tests executed, their results, and any issues or defects found  
c) Providing information about each defect, such as the steps to reproduce it  
d) Providing information on testing planned for the next period  

## justification
a) Is not correct. Tracking test progress and identifying areas that require further attention is an example of supporting the ongoing control of testing. This is one of the purposes of test reports  
b) Is not correct. Providing information on the tests executed, their results, and any issues or defects found is an example of summarizing the test activities performed at a given test level. This is one of the purposes of test reports  
c) Is correct. Providing information about defects is the purpose of a defect report, not a test report  
d) Is not correct. Providing information on testing planned for the next period is one of the purposes of test reports  

# metadata
lo: 5.4.1
k-level: K2
points: 1
correct: d

## question
The user reported a software failure. An engineer from the support team asked the user for the software version number where the failure was observed. Based on the version number, the team reassembled all the files that made up the release. This later allowed a developer to perform analysis, find the defect, and fix it.

Which of the following enabled the above activity to be performed by the team?

## answers
a) Risk management  
b) Test monitoring and control  
c) Whole-team approach  
d) Configuration management  

## justification
a) Is not correct. Risk management consists of risk analysis and risk control. Neither of these activities supports the reassembly of the files that made up the release, because these activities deal with risks, not with configuration items  
b) Is not correct. Test monitoring is concerned with gathering information about testing. This information is used to assess test progress and to measure whether the test exit criteria or the test tasks associated with the exit criteria are satisfied, such as meeting the targets for coverage of product risks, requirements, or other acceptance criteria. Test control uses the information from test monitoring to provide, in the form of control directives, guidance and the necessary corrective actions to achieve the most effective and efficient testing. None of these activities deal with the management of configuration items  
c) Is not correct. The whole-team approach builds on the tester’s skill to work effectively in a team context and to contribute positively to the team goals. So, it focuses on team-related issues, not on configuration items  
d) Is correct. Configuration management provides a discipline for identifying, controlling, and tracking work products. Configuration management keeps a record of changed configuration items when a new baseline is created. Using configuration management, it is possible to revert to a previous baseline in order to reproduce previous test results  

# metadata
lo: 5.5.1
k-level: K3
points: 1
correct: a

## question
Consider the following defect report for a Book Lending System.

```
Defect ID: 001	|	Title: Unable to Return a Book	|
Severity: High	|	Priority:	                      |
Environment: Windows 10, Google Chrome
Description: When attempting to return a book using the Book Return feature, the system does not register the return and the book remains checked out to the user.
Steps to Reproduce:
Login to the Book Lending System as a user who has checked out a book.
Click on the "Book Return" button for the book that has been checked out.
System does not register the return and the book remains checked out.
Expected Result: The book should be returned and no longer appear as checked out to the user.
Actual Result: The book remains checked out to the user and is not registered as returned in the system.
Attachments: [empty list]
```

Which of the following is MOST likely to help the developer reproduce the failure quickly?

## answers
a) Adding information about which users and which books the issue affects to the “Description” section  
b) Filling in the missing value for the “Priority” field  
c) Adding memory dumps and database snapshots taken after each step described in the “Steps to Reproduce” section to the “Attachments” section  
d) Repeating the same test case for different environments and writing defect reports for each of them separately  

## justification
a) Is correct. Adding this information allows the developer to use the same input data, so it is more likely they will be able to reproduce the failure quickly and so identify the defect faster  
b) Is not correct. Adding the value of Priority will not help in reproducing the defect itself  
c) Is not correct. Although some of this information may be of value, adding the memory dumps and database snapshots after each step will be too much, because most of these artefacts will contain useless information for the developer, and make the report less readable. It will also require the developer to spend a lot of time analyzing this information, which will lengthen the repair process  
d) Is not correct. The question was about helping the developer to reproduce the defect observed for a specific environment configuration  

# metadata
lo: 6.1.1
k-level: K2
points: 1
correct: b

## question
Given the following test tool categories:

i. Collaboration tools
ii. DevOps tools
iii. Management tools
iv. Non-functional testing tools 
v. Test design and implementation tools

Tools from which of the categories are MOST likely to facilitate test execution?

## answers
a) i, v  
b) ii, iv  
c) i, iii, v  
d) ii, iii, iv  

## justification
a) Is not correct  
b) Is correct. Both DevOps tools (ii) and Non-functional testing tools (iv) facilitate test execution  
c) Is not correct  
d) Is not correct  

# metadata
lo: 6.2.1
k-level: K1
points: 1
correct: c

## question
Which of the following is MOST likely to be a risk of test automation?

## answers
a) The detection of additional high-severity defects  
b) Providing measures that are too complicated for humans to derive  
c) Incompatibility with the development platform  
d) Substantially reduced test execution times  

## justification
a) Is not correct. The detection of additional high-severity defects would be a benefit of test automation, rather than a risk  
b) Is not correct. The provision of measures that are too complicated for humans to derive themselves is normally considered to be a benefit of test automation  
c) Is correct. If the test automation is incompatible with the development platform, then it will not be able to integrate them, and, for instance, pass test inputs to the test object and receive test results from the test object  
d) Is not correct. Substantially reduced test execution times would normally be considered a benefit that is provided by test automation  
