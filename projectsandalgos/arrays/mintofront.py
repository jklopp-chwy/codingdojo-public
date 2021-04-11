def minToFront(li):
    min = li[0]
    count = 0
    for i in li:
        if min > i:
            min = i
            count = count + 1
    li.insert(0,min)
    li.pop(count+1)
    return li, count

print(minToFront([4,2,1,3,5]))