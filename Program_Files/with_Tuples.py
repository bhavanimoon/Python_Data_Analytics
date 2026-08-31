# Tupes are immutable or unchangable. You can only get information about a tuple.
# Tuples once created cannot be mutated or changed or appended or delete items from it.

'''
Where can it be used?
Sometimes in your program you want to create a list of items that must not be changed throughout
even by accident. Tuples can be useful in such cases.
'''

num_tuple = (2, 8, 10, 14)
print(num_tuple)

# UNPACKING
dimensions = ('length', 'breadth', 'height')

# One way to utilize this if you want to multiply the dimensions
len = dimensions[0]
bth = dimensions[1]
hgt = dimensions[2]
print(len, bth, hgt)

# Other way using unpacking
l, b, h = dimensions
print(l, b, h)

# Unpacking can be done on lists too
dim_values = [4, 2.5, 7]
lv, bv, hv = dim_values
print(lv, bv, hv)