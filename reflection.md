# Reflection

Student Name:  Hassatou Daramey
Sudent Email:  hndarame

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

This assignment helped me understand how automated testing works in Python using pytest, but I ran into multiple issues that made it hard to get the tests running successfully. Specifically, when I tried running pytest, no tests were detected even though I had written and saved test functions like test_reviews_step_output() and others. At first, I didn’t realize the test file needed to start with test_ in the filename for pytest to detect it, so renaming the file was one key fix I learned.

I also encountered an ImportError in my assignment_etl.py file, where Python couldn’t find or import the function get_place_reviews from apicalls.py. This made me realize that the apicalls.py file either doesn't contain the right functions or they are not named or implemented correctly. I still need to review that file and ensure it includes get_place_reviews, analyze_sentiment, and extract_entities.

Another challenge was understanding the file structure....specifically where the cache CSVs should be stored and how to clear or re-run the ETL steps if something failed. I attempted to run rm cache/*.csv, but PowerShell couldn’t find the folder, which taught me to be more careful about checking paths and directory structures when writing or running scripts.

I feel like I understand the purpose of each test and what it is checking for: the existence of the output CSVs, whether they have the correct number of rows, and whether the expected columns are present. But I need more practice with writing importable functions, organizing testable code, and debugging Python environment issues like missing files or modules.

