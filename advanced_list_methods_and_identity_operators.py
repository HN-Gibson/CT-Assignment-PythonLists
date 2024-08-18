# Problem Statement: You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]
# Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? And how can you check to see if Alice is in both submitted and attended in one if statement?

submitted = ["Alice", "Bob", "Charlie", "David"] #list provided
attended = ["Charlie", "Eve", "Alice", "Frank"] #list provided

participant = "Alice" #set a variable that can be changed to check the participation of a student in the following if statment

#used a single if statement to produce an output for both conditions being met as well as either or no condition being met
if participant in submitted and participant in attended: #used a comparison statement with in to reference the lists and determine if the participant was in both lists
    print(f"{participant} submitted the assignment and attended the last class!")  
else:
    print(f"{participant} was not a full participant.")