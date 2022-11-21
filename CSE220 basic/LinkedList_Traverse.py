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
    
    def showList(self):
        iter = self.head
        while iter!=None:
            print(iter.data,end=" ")
            iter=iter.next

List1 = MyList([1,2,3,4,5,6])
List1.showList()