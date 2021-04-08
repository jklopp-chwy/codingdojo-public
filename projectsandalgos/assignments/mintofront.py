def minToFront(li):
    min = li[0]
    for i in li:
        if min > i:
            min = i
    li.pop(min)
    li.insert(0,min)
    return li

print(minToFront([2,1,5]))