class Cup:
        def __init__(self, materialOfCup, colorOfCup):
            self.material = materialOfCup
            self.color = colorOfCup
            self.percent_filled = 0

        def fill(self, amountOfLiquid):
            self.percent_filled += amountOfLiquid

        def pour(self, amountOfLiquid):
            self.percent_filled -= amountOfLiquid

        def spill(self):
            self.percent_filled -= self.percent_filled / 2

        def say_info(self):
            print(f"this {self.color} {self.material} cup is {self.percent_filled}% full.")

        
myFavoriteCup = Cup("paper","white")
myFavoriteCup.fill(60)
myFavoriteCup.spill()
myFavoriteCup.say_info()
