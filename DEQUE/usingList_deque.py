class Deque:
    def __init__(self) -> None:
        self.mylist=[]

    def is_empty(self):
        return len(self.mylist)==0
    
    def insert_rear(self,data):
        self.mylist.append(data)
    
    def insert_front(self,data):
        self.mylist.insert(0,data)

    def delete_rear(self):
        if not self.is_empty():
            self.mylist.pop()
        else:
            raise IndexError('No Item To Delete!')
        
    def delete_front(self):
        if not self.is_empty():
            self.mylist.pop(0)
        else:
            raise IndexError('No Item To Delete!')
        
    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError("No item at front!")
        
    def get_rear(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise IndexError("No item at front!")
        
    def size(self):
        return len(self.mylist)
    
d1=Deque()
d1.insert_front(20)
d1.insert_front(30)
d1.insert_front(40)
d1.insert_front(50)
d1.insert_front(60)
d1.insert_rear(10)
d1.delete_front()
d1.delete_rear()
print("Front = ",d1.get_front(),'Rear = ',d1.get_rear())
print("Size = ",d1.size())


        

