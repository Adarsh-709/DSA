from SLL import *

class Queue:
    def __init__(self) -> None:
        self.mylist=SLL()
        self.rear=None
        self.itemcount=0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def enqueue(self,data):
        self.mylist.insert_last(data)
        self.rear=data
        self.itemcount+=1
    def dequeue(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.itemcount-=1
        else:
            raise IndexError("Queue is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.mylist.head.item
        else:
            raise IndexError("Queue is empty")
    def get_rear(self):
        if not self.is_empty():
            return self.rear
        else:
            raise IndexError("Queue is empty")
        
    def size(self):
        return self.itemcount
    
q1=Queue()
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
q1.enqueue(70)
q1.enqueue(80)
print("Front = ",q1.get_front(),"Rear = ",q1.get_rear())
print("size = ",q1.size())
q1.dequeue()
print("Front = ",q1.get_front(),"Rear = ",q1.get_rear())
print("size = ",q1.size())