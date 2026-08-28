# Working with 2 Dimensional Lists or Matrices

matrix = [
    ['a', 'b', 'c'],
    ['apple', 'banana', 'chikoo'],
    ['ant', 'bee', 'cat'],
    ['aubergine', 'beetroot', 'cyanne pepper']
]

# Access any one item from the 2D list
print(matrix[1][2])

# Update any item within the 2D list
matrix[1][2] = 'cherry'
print(matrix[1][2])
print(matrix)

# Looping to access items inside the 2D list
for row in matrix:
    for item in row:
        print(item)

# Insert a value at a specified position in a list
numbers = [9, 3, 6, 18, 15]
# Insert a number at position 1
numbers.insert(1, 21)
print(numbers)

# Remove an item from the list
numbers.remove(6)
print(numbers)

# Clear out the entire list
numbers.clear()
print(numbers)

# Delete only the last item in the list
numbers = [9, 3, 6, 18, 15]
numbers.pop()
print (numbers)

# Access an item from the list using it's index (position)
numbers = [9, 3, 6, 18, 15, 21, 24, 27, 30]
print(numbers)
print(numbers.index(6))  # Prints out the index of number 6 in the numbers list
print(33 in numbers)  # Returns a boolean value True or False if the number is present in the list or not
print(numbers.count(15)) # Counts how many 15('s) are present in the list. Returns 1 in this case.

# Sorting the list
'''
Sort method doesn't return any value. It sorts the list in place.
Default sort is in ascending order. Use reverse=True/False to sort desc/asc.
'''
numbers = [33, 9, 3, 6, 36, 18, 15, 21, 39, 24, 27, 30]
numbers.sort(reverse=False)
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(f"numbers list sorted in reverse order:\n{numbers}")


# Remove duplicates from a list (mine)
num_list = [70, 80, 30, 41, 87, 20, 80, 70, 100, 54, 18, 13, 5]
print(f"num_list before removing duplicates:\n{num_list}")
for item in num_list:
    if num_list.count(item) > 1:
        num_list.remove(item)

print(f"num_list after removing duplicates:\n{num_list}")

# Remove duplicates from a list (another way)
num_list = [70, 80, 30, 41, 87, 20, 80, 70, 100, 54, 18, 13, 5]
uniques = []

for item in num_list:
    if item not in uniques:
        uniques.append(item)

print(f"Original list:\n{num_list}")
print(f"List of unique numbers:\n{uniques}")
