# Code for Day 5, Exercise 1

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

avg = 0

for student_height in student_heights:
    avg += int(student_height)

print(int(avg / len(student_heights)))
