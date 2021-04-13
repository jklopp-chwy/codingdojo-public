class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

##front
    def addFront(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

#remove front
    def removeFront(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
#front
    def front(self):
        current = self.head
        return current.data

#contains
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            print("Not found")
        return current
#length
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

#display
    def display(self):
        curr = self.head
        myStr = ""
        while curr:
            myStr = f" {myStr} {curr.data}"
            curr = curr.get_next()
        print(myStr)

#max
    def max(self):
        curr = self.head
        max = curr.data
        while curr:
            if curr.data > max:
                max = curr.data
            curr = curr.get_next()
        print(max)

#min 
    def min(self):
        curr = self.head
        min = curr.data
        while curr:
            if curr.data < min:
                min = curr.data
            curr = curr.get_next()
        print(min)

#average
    def average(self):
        curr = self.head
        sum = 0
        count = 0
        while curr:
            sum = sum + curr.data
            count = count + 1
            curr = curr.get_next()
        avg = sum/count
        print(avg)

myList = LinkedList()
myList.addFront(5)
myList.addFront(15)
myList.addFront(25)
myList.addFront(50)
myList.addFront(300)
myList.addFront(100)
print("Printing")
myList.display()
myList.max()
myList.min()
myList.average()