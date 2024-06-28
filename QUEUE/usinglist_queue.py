class Queue:
    def __init__(self) -> None:
        self.mylist=[]
        self.itemcount=0
        self.rear=None
        self.front=None

    def is_empty(self):
        return len(self.mylist)==0
    
    def enqueue(self,data):
        self.mylist.append(data)
        self.rear=data
        self.front=self.mylist[0]
        self.itemcount+=1

    def dequeue(self):
        if not self.is_empty():
            self.mylist.pop(0)
            self.itemcount-=1
            if self.is_empty():
                self.front=None 
                self.rear=None 
            else: 
                self.front=self.mylist[0]
        else:
            raise IndexError("Queue is empty! Cannot Dequeue")

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.rear
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.front
    def size(self):
        return self.itemcount
    
s1=Queue()
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
s1.enqueue(40)
s1.enqueue(50)
s1.enqueue(60)
s1.dequeue()
s1.dequeue()
print("Front element is:",s1.front)
print("Rear element is:",s1.rear)
print("Length of Queue is:",s1.itemcount)

