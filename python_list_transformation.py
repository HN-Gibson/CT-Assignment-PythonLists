# Problem Statement: You've been given a list of grades from an exam. You need to process and analyze these grades.

#Task 1: Given the list of grades:

#grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

#Sort the grades in descending order and print the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93] #list of grades provided
grades.sort() #sorts the grades in ascending order
grades.reverse() #reverses the order of the list to give descending list
print (grades) #prints the list in descending order

#Task 2: Calculate the average grade and print it.

average_grade = sum(grades)/len(grades) #assigns the average of the sum of the list divided by the len (number of indices) to the average_grade variable
print(average_grade) #prints the average grade variable