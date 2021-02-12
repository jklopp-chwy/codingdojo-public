# def biggie_size(list):
#     for i in range(len(list)):
#         if list[i] >= 0:
#             list[i] = "big"
#         return list

# print(biggie_size([-10,-5,0,1,5,10]))

#Given a list of numbers, create a function to replace the last value with the number of positive values.

# def count_positives(list):
#     count = 0
#     for i in list:
#         if i > 0:
#             count = count + 1
#     list.pop((len(list)) - 1)
#     list.append(count)
#     return(list)

# print(count_positives([-1,-1,1,2,3]))

#Create a function that takes a list and returns the sum of all the values in the array.

# def sumtotal(list):
#     total = 0
#     for i in list:
#         total = total + i
#     return(total)

# print(sumtotal([1,2,4]))

#Create a function that takes a list and returns the average of all the values

# def average(list):
#     total = 0
#     for i in list:
#             total = total + i
#     average = total/len(list)
#     return average

# print(average([1,2,3,4]))

#Create a function that takes a list and returns the length of the list.
# def length(list):
#     length = len(list)
#     return length

# print(length([1,2,3,4]))

# Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# def minimum(list):
#     min = list[0]
#     for i in list:
#         if min > i:
#             min = i
#     return min

# print(minimum([2,1,5]))

#Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# def maximum(list):
#     min = list[0]
#     for i in list:
#         if min < i:
#             min = i
#     return min

# print(maximum([2,1,5,1,10,1]))

#Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

def ultimate(list):
    sum = 0
    for i in list:
        sum = sum + i

    count = 0
    for i in list:
            count = count + i
    average = count/len(list)

    min = list[0]
    for i in list:
        if min > i:
            min = i

    max = list[0]
    for i in list:
        if max < i:
            max = i

    length = len(list)

    dictionary = dict()
    dictionary['sum'] = sum
    dictionary['average'] = average
    dictionary['minimum'] = min
    dictionary['maximum'] = max
    dictionary['length'] = length
    
    return(dictionary)
print(ultimate([1,2,3,4,100]))

#Create a function that takes a list and return that list with values reversed. Do this without creating a second list.

#def reverse(list):