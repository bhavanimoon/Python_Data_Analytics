import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        # return (first, second)
        return first, second


'''
In Python when a funciton returns a tuple, it need not be placed within ().
It works just fine when you write "return first, second"
'''

dice_roll = Dice()
print(dice_roll.roll())