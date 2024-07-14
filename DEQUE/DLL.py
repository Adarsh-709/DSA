                                            #DOUBLY LINKED LIST

class Node:
    def __init__(self,prev=None,item=None,next=None) -> None:
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None) -> None:
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_at_first(self,data):
        if self.is_empty():
            n=Node(None,data,None)
            self.start=n
        else:
            n=Node(None,data,self.start)
            self.start.prev=n
            self.start=n

    def insert_at_last(self,data):
        if self.is_empty():
            n=Node(None,data,None)
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            n=Node(temp,data,None)
            temp.next=n

    def search(self,data):
        if self.is_empty():
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    return temp
                temp=temp.next

    def insert_after(self,aft,data):
        if self.is_empty():
            pass
        else:
            temp=self.search(aft)
            if temp.next==None:
                self.insert_at_last(data)
            else:
               n=Node(temp,data,temp.next)
               temp.next.prev=n
               temp.next=n

    def insert_before(self,bef,data):
        if self.is_empty():
            pass
        else:
            temp=self.search(bef)
            if temp.prev==None:
                self.insert_at_first(data)
            else:
                n=Node(temp.prev,data,temp)
                temp.prev.next=n
                temp.prev=n

    def delete_first(self):
        if self.is_empty():
            pass
        elif self.start.next==None:
            self.start=None
        else:
            self.start.next.prev=None
            self.start=self.start.next

    def delete_last(self):
        if self.is_empty():
            pass
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None

    def delete_item(self,data):
        if self.is_empty():
            pass
        elif self.start.item==data:
            self.delete_first()
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next==None:
                        self.delete_last()
                    else:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev

                temp=temp.next

    def printlist(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next

    def __iter__(self):
        return DLLIterator(self.start)


#CREATING THE ITERATOR FOR OUR LIST
class DLLIterator:
    def __init__(self,start) -> None:
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

'''dll=DLL()
dll.insert_at_first(2)
dll.insert_at_last(3)
dll.insert_at_last(5)
dll.insert_at_last(6)
dll.insert_at_last(7)
dll.insert_at_last(8)
dll.insert_after(3,4)
dll.insert_after(8,9)
dll.insert_before(2,1)
dll.insert_before(3,2.5)
dll.insert_before(9,8.5)

#USING THE ITERATOR TO PRINT
for x in dll:
    print(x,end=" ")'''


            