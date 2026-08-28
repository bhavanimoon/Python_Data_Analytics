# Single For Loop
# Calculate the total cost of your shopping cart

cart_items = ['Banana', 'Kurkure', 'Ragi Rotti']
cart_values = [120, 50, 200]
total_cost = 0

for item in cart_values:
    # total_cost = total_cost + int(item)
    total_cost += item
# print("Total cost of shopping cart is: " + str(total_cost))
print(f"Total value: {total_cost}\n")

# Nested for loop
# Print a matrix (x, y) of whole numbers

x = int(input("Input x value: "))
y = int(input("Input y value: "))

for x_item in range(x):
    for y_item in range(y):
        print(f"{x_item}, {y_item}")
print('\n')

# Print letter F using *
# Simple code using Python multiplier feature
f_numbers = [8, 2, 2, 5, 2, 2, 2]

# print(f_count)
for item in f_numbers:
    print("*" * item)

# Using Nested For loop
print('\n')
for item in f_numbers:
    print_value = ''
    for counter in range(item):
        print_value += '*'
    print(print_value)

# Write a program to find the largest & smallest number in a list
num_list = [9, 10, 2, 99, 30, 45, 1, 0, 87, 20]
largest = num_list[0]
smallest = num_list[0]
for item in num_list:
    if item >= largest:
        largest = item
    if item <= smallest:
        smallest = item

print(f"Largest number from the num_list is: {largest}")
print(f"Smallest number from the num_list is: {smallest}")

# Sort the list of numbers smallest to largest or vice versa using sort() function
numbers = [89, 0, 23, 46, 12, 90, 184, 22, 75]
numbers.sort(reverse=True)
print(f"Sorted numbers list in descending order:\n {numbers}")
print(f"Largest number from the numbers list is: {numbers[0]}")

numbers.sort(reverse=False)
print(f"Sorted numbers list in ascending order:\n {numbers}")
print(f"Smallest number from the numbers list is: {numbers[0]}")
    