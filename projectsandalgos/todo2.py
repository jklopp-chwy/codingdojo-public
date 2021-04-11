#using lots of list slices, need to continue to learn about them
#given an array, reverse the order of values.

#def reverse(list):
        #return(list[::-1])
#my_list = [1,2,3,4,5]
##print(reverse(my_list))

#define a function that accepts an array and offset. shift array to the right by that amount and rotate.

#def rotate(list, offSet):
    #offSet = -offSet % len(list)
    #return list[offSet:] + list[:offSet]
#my_list = [1,2,3,4,5]
#print(rotate(my_list, 1))

#given an array and two values, remove all values in the array that
#def filterRange(list, min, max):
    #min = min
    #max = max
    #for i in list:
        #if i > max:
            #max = i
    #list.pop(i-1)
    #for i in list:
        #if i < min:
            #min = i
    #return list 
#my_list = [1,2,3,5,4]
#print(filterRange(my_list, 1, 2))

#def filterRange(list, min, max):
    #tempArr = []
    #for i in list:
        #if i < max and i > min:
            #tempArr.append(i)
    #return tempArr 
#my_list = [10,51,4,3,2,20]
#print(filterRange(my_list, 1, 5))

def concat(list1,list2):
    newList = list1 + list2
    return newList
myList1 = [1,2,3]
myList2 = ['a','b']
print(concat(myList1, myList2))