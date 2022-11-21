class Node:
    def __init__(self, data=None, next=None):
        self.element = data
        self.next = next

class MyList:
    #Creating Constractor
    def __init__(self,datas=None):
        if datas is None:
            self.head = None
            
        elif isinstance(datas,list):
            self.head = Node(datas[0],None)
            indexnode = self.head
            for data in datas:
                indexnode.next = Node(data,None)
                indexnode = indexnode.next
        else:
            print("Wrong Data Type")
    def showList(self):
        iter = self.head
        while iter!=None:
            print(iter.element,end=" ")
            iter=iter.next
            
List1 = MyList([1,2,3,4,5,6])
List1.showList()