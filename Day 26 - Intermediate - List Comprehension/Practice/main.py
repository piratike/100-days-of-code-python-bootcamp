# Code for Day 26 practice

numbers = [1, 2, 3]
new_numbers = [number + 1 for number in numbers]
print(new_numbers)

numbers = [number * 2 for number in range(1, 5)]
print(numbers)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
large_names = [name.upper() for name in names if len(name) > 5]

print(short_names, large_names)
