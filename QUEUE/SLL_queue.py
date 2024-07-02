class Node:
    def __init__(self,item=None,next=None) -> None:
        self.item=item
        self.next=next
class Queue:
    def __init__(self) -> None:
        self.front=None
        self.rear=None
        self.itemcount=0

    def is_empty(self):
        return self.rear==None and self.front==None
    
    def enqueue(self,data):
        if self.is_empty():
            n=Node(data)
            self.front=n
            self.rear=n
        else:
            n=Node(data)
            self.rear.next=n
            self.rear=n
        self.itemcount+=1
    def dequeue(self):
        if not self.is_empty():
            self.front=self.front.next
            self.itemcount-=1
        else:
            raise IndexError("No Elements To dequeue")
    
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("No Elements At Front")
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("No Elements At rear")
        
    def size(self):
        return self.itemcount
    
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("Front = ",q1.get_front(),"Rear = ",q1.get_rear())
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.enqueue(1)
print("Front = ",q1.get_front(),"Rear = ",q1.get_rear())
print("Size of Queue is : ",q1.size())


    
        


