# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print(x[1])
# students[0]['last_name'] = 'bryant'
# print(students)
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])
# z[0]['y']=30
# print(z)

students = [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(some_list):
#     for i in range (len(some_list)):
#         name_dict = some_list[i]
#         for key, value in name_dict.items():
#             print(key, ':', value)
#iterateDictionary(students)

# def iterateDictionary2(key_name, some_list):
#     x = key_name
#     for i in range (len(some_list)):
#         name_dict = some_list[i]
#         for key, value in name_dict.items():
#             if key == x:
#                 print(value)
# iterateDictionary2('first_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
            #print((len(some_dict[key])) + " " + key)
            title = f"{len(some_dict[key])} {key}"
            print(title)
            for x in some_dict[key]:
                print(x)
printInfo(dojo)
