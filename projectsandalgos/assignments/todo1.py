def pushFront(li, num):
    x = [num] + li
    return x

print(pushFront([1,2,3], 0))

# def popFront(li):
#     x = li[0]
#     li.pop(0)
#     return x,li

# print(popFront([1,2,3]))

# def insertAt(li, num, pos):
#     li = li
#     li[pos] = pos
#     return li

# print(insertAt([1,2,3], 0, 2))

# def removeAt(li, num):
#     x = li[num]
#     num = num
#     li.pop(num)
#     return x, li
# print(removeAt([1,2,3], 2))

# def removeDups(li):
#     arr = []
#     for i in li:
#         if i != li[i]:
#             arr.append(i)
#     return arr

# print(removeDups([1,1,2,2,3]))