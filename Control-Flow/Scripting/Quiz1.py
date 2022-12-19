"""
Write a script that does the following:

1. Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades. Use this input to create lists for names, assignments, and grades.
2. Use a loop to print the message for each student with the correct values. The potential grade is simply the current grade added to two times the number of missing assignments.

"""

names =  tuple(input("Enter names separated by commas: ").title().split(','))# get and process input for a tuple of names
assignments =  tuple(input("Enter assignment counts separated by commas: ").split(','))# get and process input fortuple list of the number of assignments
grades =  tuple(input("Enter grades separated by commas: ").split(','))# get and process input for a list tuple grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
