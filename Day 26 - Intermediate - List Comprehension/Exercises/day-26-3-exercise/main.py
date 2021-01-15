# Code for Day 26, Exercise 3

with open('file1.txt') as numbers1:
    data1 = numbers1.readlines()

with open('file2.txt') as numbers2:
    data2 = numbers2.readlines()

result = [int(number) for number in data1 if number in data2]

print(result)
