from DLL import *

class Deque(DLL):
    def __init__(self, start=None) -> None:
        super().__init__(start)
        self.count=0

    def is_empty(self):
        return super().is_empty()
    
    def insert_front(self,data):
        self.insert_at_first(data)
        self.count+=1

    def insert_rear(self,data):
        self.insert_at_last(data)
        self.count+=1

    def delete_front(self):
        if not self.is_empty():
            self.delete_first()
            self.count-=1
        else:
            raise IndexError("No Element To Delete")
        
    def delete_rear(self):
        if not self.is_empty():
            self.delete_last()
            self.count-=1
        else:
            raise IndexError("No Element To Delete")
        
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("No Element at front")     

    def get_rear(self):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            return temp.item
        else:
            raise IndexError("No Element at front")
        
    def size(self):
        return self.count
    
    def delete_item(self, data):
        raise AttributeError('No Such Attribute')
    
    def insert_after(self, aft, data):
        raise AttributeError('No Such Attribute')
        
    def insert_before(self, bef, data):
        raise AttributeError('No Such Attribute')
    
    def printlist(self):
        raise AttributeError('No Such Attribute')
        
    def search(self, data):   
        raise AttributeError('No Such Attribute')
       
d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_rear(40)
d1.insert_rear(50)
d1.insert_rear(60)
d1.delete_front()
d1.delete_rear()
print('Front :',d1.get_front())
print('Rear :',d1.get_rear())
print('Size :',d1.size())