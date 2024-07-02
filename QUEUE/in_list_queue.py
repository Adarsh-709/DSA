from sys import maxsize
from typing import SupportsIndex


class Queue(list):
    def is_empty(self):
        return len(self)==0
    def enqueue(self,data):
        self.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.pop(0)
        else:
            raise IndexError("Queue Underflow")
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Queue Underflow")
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Queue Underflow")
    def size(self):
        return len(self)
    

    def insert(self, index: SupportsIndex, object) -> None:
        raise AttributeError("No such Attribute 'insert' Exists in Queue")
    def remove(self, value) -> None:
        raise AttributeError("No such Attribute 'remove' Exists in Queue")
    def reverse(self) -> None:
        raise AttributeError("No such Attribute 'reverse' Exists in Queue")
    def index(self, value, start: SupportsIndex = 0) -> int:
        raise AttributeError("No such Attribute 'index' Exists in Queue")
        
        
        

q1=Queue()

try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
try:
    print(q1.index(30))
except AttributeError as e:
    print(e.args[0])
print("Size of Queue is now : ",q1.size())
print("Front = ",q1.get_front(),"Rear = ",q1.get_rear())
try:
    q1.dequeue()
    print("Size of Queue is now : ",q1.size())
except IndexError as e:
    print(e.args[0])
print("Front = ",q1.get_front(),"Rear = ",q1.get_rear())


