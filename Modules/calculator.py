import utils
# from converter import square

# print(square(4))
print(utils.square(3))
print(utils.cube(10))

numbers = [9, 10, 45, 32, 2, 29, 98, 21, 38]
max_num = utils.max(numbers)
print(f"Largest number is {max_num}")

print(max(numbers))