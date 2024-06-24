class Node:
    def __init__(self,prev=None,item=None,next=None) -> None:
        self.prev=prev
        self.item=item
        self.next=next
class CDLL:
    def __init__(self,start=None) -> None:
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_first(self,data):
        if self.is_empty():
            n=Node(None,data,None)
            self.start=n
        elif self.start.next==None:
            n=Node(self.start,data,self.start)
            self.start.prev=n
            self.start.next=n
            self.start=n
        else:
            n=Node(self.start.prev,data,self.start)
            self.start.prev.next=n
            self.start.prev=n
            self.start=n
    def insert_last(self,data):
        if self.is_empty():
            n=Node(None,data,None)
            self.start=n
        elif self.start.next==None:
            n=Node(self.start,data,self.start)
            self.start.prev=n
            self.start.next=n
        else:
            n=Node(self.start.prev,data,self.start)
            self.start.prev.next=n
            self.start.prev=n

    def search(self,data):
        if self.is_empty():
            pass
        temp=self.start
        while True:
            if temp.item==data:
                return temp
            temp=temp.next

    def insert_after(self,aft,data):
        temp=self.search(aft)
        if temp==self.start.prev:
            self.insert_last(data)
        else:
            n=Node(temp,data,temp.next)
            temp.next.prev=n
            temp.next=n
    
    def delete_first(self):
        if self.is_empty():
            print("List is empty")
        else:
            self.start.prev.next=self.start.next
            self.start.next.prev=self.start.prev
            self.start=self.start.next
    
    def delete_last(self):
        if self.is_empty():
            print("List is empty")
        else:
            self.start.prev.prev.next=self.start
            self.start.prev=self.start.prev.prev
    
    def delete_item(self,data):
        temp=self.search(data)
        if temp==self.start:
            self.delete_first()
        elif temp==self.start.prev:
            self.delete_last()
        else:
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
        
    def print(self):
        if self.is_empty():
            pass
        else:
            temp=self.start
            while temp!=self.start.prev:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item,end=" ")

    def __iter__(self):
        return CDLLIterator(self.start)
    
class CDLLIterator:
    def __init__(self,start,count=0) -> None:
        self.current=start
        self.start=start
        self.count=count
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        self.count=1
        return data

mylist=CDLL()
mylist.insert_first(0)
mylist.insert_last(1)
mylist.insert_last(3)
mylist.insert_last(4)
mylist.insert_last(5)
mylist.insert_last(6)
mylist.insert_after(1,2)
mylist.insert_after(6,7)
mylist.delete_item(5)
mylist.delete_item(7)
mylist.delete_item(0)
#mylist.print()
for x in mylist:
    print(x,end=" ")