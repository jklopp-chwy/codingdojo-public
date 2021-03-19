# #countdown
# def countdown(x):
#     for x in range(x , 0, -1):
#         print(x)
# print(countdown(5))

#print and return

# def printandreturn(x,y):
#     print(x)
#     return(y)
# print(printandreturn(4,1))

#Firstpluslength

# def firstpluslength(z):
#     length = len(z)
#     number = z[0]
#     total = length + number
#     return(total)

# mylist = [1,2,3]
# print(firstpluslength(mylist))

#valuesgreaterthansecond

# def valuesgreaterthansecond(a):
#     greater = a[1]
#     count = len(a) - 1
#     newlist = []
#     x = 0

#     while x <= count:
#         if a[x] <= greater:
#             x = x + 1
#         else:
#             newlist.append(a[x])
#             x = x + 1
#     print(len(newlist))
#     return(newlist)

# mylist = [5,2,3,2,1,4]
# print(valuesgreaterthansecond(mylist))

#thislengththatvalue

def thislengththatvalue(a,b):
    length = a
    value = b
    x = 0
    mylist = []
    while x <= a:
        mylist.append(value)
        x = x + 1
    return mylist

print(thislengththatvalue(4,7))
