                                            #SINGLY LINKED LIST

class Node:
    def __init__(self,item=None,next=None) -> None:
        self.item=item
        self.next=next

class SLL:
    def __init__(self,head=None) -> None:
        self.head=head
    
    def is_empty(self):
        return self.head==None
    
    def insert_first(self,data):
        n=Node(data,self.head)
        self.head=n

    def insert_last(self,data):
        temp=self.head
        n=Node(data)
        while temp.next is not None:
            temp=temp.next
        temp.next=n

    def search(self,data):
        temp=self.head
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
    
    def insert_after(self,aft,data):
        temp=self.search(aft)
        n=Node(data,temp.next)
        temp.next=n
    def delete_first(self):
        if self.head is None:
            pass
        else:
            self.head=self.head.next
    
    def delete_last(self):
        if self.head is None:
            pass
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    def delete_item(self,data):
        if self.head is None:
            pass
        else:
            temp=self.head
            while temp.next is not None:
                if temp.next.item ==data:
                    temp.next=temp.next.next
                temp=temp.next
                
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next

    def __iter__(self):
        return SLLIterator(self.head)

#CREATING THE ITERATOR FOR OUR LIST
class SLLIterator:
    def __init__(self,head) -> None:
        self.current=head
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    
mylist=SLL()
mylist.insert_first(10)
mylist.insert_last(15)
mylist.insert_first(0)
mylist.insert_after(0,5)
mylist.insert_last(20)
mylist.printlist()
print()
mylist.delete_first()
mylist.delete_last()
mylist.delete_item(10)

#PRINTING THE ELEMENTS USING ITERATOR
for x in mylist:
    print(x,end=" ")
    

