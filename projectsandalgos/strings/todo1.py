def removeBlanks(mystr):
    return "".join(mystr.split())
string = 'p l a y that f un ky mus ic'
print(removeBlanks(string))

def getDigits(myStr):
    return "".join([i for i in myStr if i.isdigit()])
string1 = "005123125sdfzSDFGsdfgh21345235"
print(getDigits(string1))

def acronyms(myStr):
    def cap(word):
        cap = word[0].upper()+ " "
        return cap
    myList = myStr.split()
    newWord = ""
    for word in myList:
        newWord = newWord + cap(word)
    return newWord
string2 = "the quick brown fox jumps over the lazy dog"
print(acronyms(string2))

def countNonSpaces(myStr):
    count = len("".join(myStr.split()))
    return count
string3 = "abc abc"
print(countNonSpaces(string3))

def removeShort(arr, value):
    tempArr = []
    for word in arr:
        length = len(word)
        if length > value:
            tempArr.append(word)
    return tempArr
array1 = ["my", "cat", "love", "pizza"]
print(removeShort(array1, 4))