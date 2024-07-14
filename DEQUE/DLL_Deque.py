class Node:
    def __init__(self,prev=None,item=None,next=None) -> None:
        self.prev=prev
        self.item=item
        self.next=next
class Deque:
    def __init__(self,start=None) -> None:
        self.front=None
        self.start=start
        self.rear=None
        self.count=0

    def is_empty(self):
        return self.start==None
    
    def insert_front(self,data):
        if self.is_empty():
            n=Node(None,data,self.start)
            self.start=n
            self.front=self.start
            self.rear=self.start
        else:
            n=Node(None,data,self.start)
            self.start.prev=n
            self.start=n
            self.front=self.start
        self.count+=1
    def insert_rear(self,data):
        if self.is_empty():
            n=Node(None,data,self.start)
            self.start=n
            self.rear=self.start
            self.front=self.start
        else:
            n=Node(self.rear,data,self.rear.next)
            self.rear.next=n
            self.rear=n
        
        self.count+=1
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError("No Element In Deque")
        else:
            self.count-=1
            if self.start.next==None:
                self.start=None
            else:
                self.start.next.prev=None
                self.start=self.start.next
                self.front=self.start

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("No Element In Deque")
        else:
            self.count-=1
            if self.start.next==None:
                self.start=None
            else:
                self.rear.prev.next=None
                self.rear=self.rear.prev

    def get_front(self):
        if self.is_empty():
            raise IndexError("No Element In Deque")
        else:
            return self.front.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No Element In Deque")
        else:
            return self.rear.item
        

    def size(self):
        return self.count
        
d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_rear(40)
d1.insert_rear(50)
d1.delete_front()
d1.delete_front()
d1.delete_rear()
print("Front :",d1.get_front())
print("Rear :",d1.get_rear())
print("Size :",d1.size())

         




