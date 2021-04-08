#1 #will print 1-9
#for i in range(1, 10, 1):
    #print(i)


# #will print 1,4,7
#for t in range(1, 10, 3):
    #print(t)


#3 will print 0,1,2,y is 3, 4 WRONG
#for y in range(5):
#    if y < 5:
#        print(y)
#    elif y == 3:
#        print("y is 3")

#4 will print 20,17,14,11,8,5,2
#for j in range(20, 1, -3):
#    print(j)

#5 will print each item in list
#cities = ["London", "Paris", "Tokyo"]
#for city in cities:
#    print(city)

#6 will print 0, 7, 1, 13, 2, 8, 3, 42, the answer
#numbers = [7, 13, 8, 42]
#for x in range(0, len(numbers)):
#    print(x)
#    print(numbers[x])
#if numbers[len(numbers) - 1] == 42:
#    print("The answer to life, the universe, and everything.")

#7 will print hello, 1, hello, 3, hello, world, 5, hello, 7, world, 9
#for num in range(10):
#    if num % 2 == 0:
#        print("Hello")
#    elif num % 4 == 0:
#        print("World")
#    else:
#        print(num)

#8 hello, 1, world, 3, hello, 5, world, 7, hello, 9
#for num in range(10):
#    if num % 4 == 0:
#        print("Hello")
#    elif num % 2 == 0:
#        print("World")
#    else:
#        print(num)

#9 1, fido, 2, 4, 3, rolls over WRONG
#pet_info = {
#    "name": "Fido", 
#    "age": 4, 
#    "trick": "rolls over"
#}
#for key in pet_info:
#    print(key)
#    print(pet_info[key])

#10 will print out the list in order with the concatination
things_to_remember = {
    "First": "use the 20 minute rule and use the platform and other resources to find my answer",
    "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
    "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
    "Fourth": "ask an available instructor"
}
for num, step in things_to_remember.items():
    print(num + ", I will " + step)

