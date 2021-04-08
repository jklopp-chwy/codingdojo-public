import random
def randInt(min=0, max=100):
    range = max - min
    if range <= 0:
        number = "range must be a positive number!"
        return number
    else:
        number = random.random() * range + min
        return round(number)
print(randInt(min=0, max =10))
