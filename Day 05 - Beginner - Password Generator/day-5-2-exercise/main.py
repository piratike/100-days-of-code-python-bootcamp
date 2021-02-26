# Code for Day 5, Exercise 2

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max_score = 0

for score in student_scores:
    if max_score < int(score):
        max_score = int(score)

print('The highest score in the class is: {}'.format(max_score))
