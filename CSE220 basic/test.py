class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class MyList:
    #Creating Constractor
    def __init__(self,datas=None):
        if datas is None:
            self.head = None
            
        elif isinstance(datas,list):
            self.head = None
            self.insert_values(datas)
        else:
            print("Wrong Data Type")

    # Inserting Values at the Beginning
    def __insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node


    # Inserting Values at the ending
    def insert(self, data, index=None):
        if index is None:
            if self.head is None:
                self.head = Node(data, None)

                return
            itr = self.head
            existance=False
            while itr.next:
                if itr.data==data:
                    print(f"{data} already exists in the list")
                    existance=True
                    break
                itr = itr.next
            if not existance:
                if itr.data==data:
                    print(f"{data} already exists in the list")
                else:
                    itr.next = Node(data, None)

        else:
            self.__insert_at(index,data)

    # Inserting Values From List at the end
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert(data)

    # Get the length of the linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    #Inserting Values by given index
    def __insert_at(self, index, data):
        if (index < 0 or index >= self.get_length()) and self.isEmpty():
            raise Exception("Invalid Index")
        existance=False
        itr = self.head
        while itr:
            if itr.data==data:
                print(f"{data} already exists in the list")
                existance=True
                break
            itr = itr.next
        if existance==False:
            if index == 0:
                self.__insert_at_beginning(data)
                return
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    #Removing a specific element
    def remove(self, data):
        if self.isEmpty():
            print("The list is already empty")
        else:
            if data == self.head.data:
                self.head = self.head.next
                return
            itr = self.head
            while itr.next:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    break
                itr = itr.next
    #Printing the linked list
    def showList(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr[:-3])
    #Chacking the list if it's empty or not
    def isEmpty(self):
        return True if self.head is None else False
    #Clearing the list
    def clear(self):
        if not self.isEmpty():
            self.head=None
        else:
            print("The linked List is already empty.")

    # Task:3-1-Making a linked list with the even elements
    def even(self):
        even_ll = MyList([])
        itr = self.head
        while itr:
            if itr.data % 2 == 0:
                even_ll.insert(itr.data)
            itr = itr.next
        even_ll.showList()

    # Task:3-2-Checking if an element is in the linked list
    def check_ele(self, ele):
        itr = self.head
        while itr:
            if itr.data == ele:
                return True
            itr = itr.next
        return False

    # Task:3-3-Reversing a list
    def reverse_ll(self):
        itr = self.head
        temp1 = None
        while itr:
            temp2 = itr.next
            itr.next = temp1
            temp1 = itr
            itr = temp2
        self.head = temp1
    #Task:3-4-Sorting the entire linked list
    def sort(self):
        itr = self.head
        while itr:
            itr2=itr
            min=itr2
            while itr2.next:
                if min.data>itr2.data:
                    min=itr2
                itr2=itr2.next
            if min.data > itr2.data:
                min = itr2
            if min!=None and itr.data>itr2.data:
                itr.data,min.data=min.data,itr.data
            itr=itr.next
    #Task:3-5-Finding out the sum of all elements in a list
    def sum(self):
        itr = self.head
        sum=0
        while itr:
            sum+=itr.data
            itr = itr.next
        print(sum)
    #Task:3-6-Rotating a linked list K times in the linked list in the right or left direction
    def rotate(self,turn,times):
        if turn.lower()=="left":
            temp=self.head
            itr=self.head
            count=0
            temp2=None
            for x in range(times):
                count+=1
                if count==times:
                    temp2=itr
                itr=itr.next
            if temp2 is not None:
                temp2.next=None
            self.head=itr
            itr2=self.head
            while itr2.next:
                itr2=itr2.next
            itr2.next=temp


        elif turn.lower()=="right":
            temp = self.head
            itr = self.head
            count = 0
            loop=self.get_length()-times
            temp2 = None
            for x in range(loop):
                count += 1
                if count == loop:
                    temp2 = itr
                itr = itr.next
            if temp2 is not None:
                temp2.next = None
            self.head = itr
            itr2 = self.head
            while itr2.next:
                itr2 = itr2.next
            itr2.next = temp
    #Making the linked list iterative/iteratable
    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.data
            itr = itr.next


ll1 = MyList([3,2,5,1,8])

ll2=MyList([3,2,5,1,8])

ll2.showList()
print(ll2.isEmpty())

ll2.clear()
print(ll2.isEmpty())

ll2.insert(1)
ll2.insert(1)
ll2.insert(2)
ll2.insert(5)
ll2.insert(8)
ll2.insert(3,3)
ll2.insert(15,2)

ll2.showList()

ll2.remove(15)
ll2.showList()

ll2.even()
print(ll2.check_ele(2))
print(ll2.check_ele(15))

ll2.reverse_ll()
ll2.showList()

ll2.sort()
ll2.showList()

ll2.sum()

ll2.rotate("left",2)
ll2.showList()

ll2.rotate("right",3)
ll2.showList()