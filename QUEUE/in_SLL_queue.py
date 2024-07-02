from LINKEDLIST.SLL import *

class Queue(SLL):
    def __init__(self, head=None) -> None:
        super().__init__(head)
        self.itemcount=0
        self.rear=None
    def is_empty(self):
        return super().is_empty()
    def enqueue(self,data):
        self.insert_last(data)
        self.rear=data
        self.itemcount+=1
    def dequeue(self):
        self.delete_first()
        self.itemcount-=1
    def get_front(self):
        if not self.is_empty():
            return self.head.item
        else:
            raise IndexError("Queue Underflow")
    def get_rear(self):
        return self.rear
    
    def size(self):
        return self.itemcount
    
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print("Front = ",q1.get_front(),"Rear = ",q1.get_rear())
q1.dequeue()
print("Size = ",q1.size())
print("Front = ",q1.get_front(),"Rear = ",q1.get_rear())

        
    

    

