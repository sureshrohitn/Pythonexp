import random


class Dice:
    def Rolling(self):
        a=random.randint(1,6)
        b=random.randint(1,6)
        return a,b


dice=Dice()
print(dice.Rolling())