from random import choice 
from pathlib import Path 

class Dice:
    def roll(self):
        set1 = choice(dice)
        set2 = choice(dice)
        return (set1, set2)
    

dice = [1,2,3,4,5,6]
print(Dice.roll(dice))
path = Path()
print(path.exists())
