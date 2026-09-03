'''
# Import Packages - option 1
import ecommerce.shipping

ecommerce.shipping.calc_shipping()

# Option 2 - from package.module import function
from ecommerce.shipping import calc_shipping

calc_shipping()
'''

# Option 3 - from package import module
# With this all functions inside the imported module can be accessed using module.funciton_name()
from ecommerce import shipping
import random

shipping.calc_shipping()
print("\n")

for i in range(3):
    print(random.random())

print("\n")

for i in range(3):
    print(random.randint(10, 20))

# random() function generates random values between 0 & 1
# randint() function generates random values between the specified range

# Pick a random item from the list
baby_animals = ['bunny', 'panda', 'kitty', 'puppy', 'cub' ]
baby_chosen = random.choice(baby_animals)
print(f"Chosen baby animal - random choice = {baby_chosen}")

# Roll the dice to check what number you are getting.
dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

print(f"({random.choice(dice1)}, {random.choice(dice2)})")
