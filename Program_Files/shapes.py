# Print shapes - diamond, square, triangle.

# Square
size = int(input(">> Input square size:-  "))

print("\n Trying to print a square")
for r in range(size):
    string = ''
    for c in range(size):
        string = string + ' o'
        c += 1
    r += 1
    print(string)


# Triangle
tri = int(input(">> Input triangle size:-  "))
r = 1
c = 1
# col = tri + (tri - 1)
print("Trying to print a right angle triangle")

while r <= tri:
    string = ""
    while c <= r:
        string = string + "* "
        c += 1
    r += 1
    c = 1
    print(string)


