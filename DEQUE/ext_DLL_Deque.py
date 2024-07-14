from DLL import *
class Deque:
    def __init__(self) -> None:
        self.mylist=DLL()
        self.rear=None
        self.itemcount=0
        
    def is_empty(self):
        return self.mylist.is_empty()
    
    def insert_front(self,data):
        self.mylist.insert_at_first(data)
        self.itemcount+=1
    
    def insert_rear(self,data):
        self.mylist.insert_at_last(data)
        self.itemcount+=1

    def delete_front(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.itemcount-=1
        else:
            raise IndexError("No Item To Delete")
        
    def delete_rear(self):
        if not self.is_empty():
            self.mylist.delete_last()
            self.itemcount-=1
        else:
            raise IndexError("No Item To Delete")
        
    def get_front(self):
        if not self.is_empty():
            return self.mylist.start.item
        else:
            raise IndexError("No Item at Front")
        
    def get_front(self):
        if not self.is_empty():
            return self.mylist.start.item
        else:
            raise IndexError("No Item at Front")
        
    def get_rear(self):
        if not self.is_empty():
            temp=self.mylist.start
            while temp.next is not None:
                temp=temp.next
            return temp.item
        else:
            raise IndexError("No Item at Front")
    
    def size(self):
        return self.itemcount
    
d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_front(40)
d1.insert_rear(50)
d1.insert_rear(60)
d1.delete_front()
d1.delete_rear()
print('Front :',d1.get_front())
print('Rear :',d1.get_rear())
print('Size :',d1.size())
        
