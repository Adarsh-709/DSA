class Deque(list):
    def is_empty(self):
        return len(self)==0
    def insert_front(self,data):
        self.insert(0,data)
    def insert_rear(self,data):
        self.append(data)
    def delete_front(self):
        if not self.is_empty():
            self.pop(0)
        else:
            raise IndexError("No item To delete")
    def delete_rear(self):
        if not self.is_empty():
            self.pop()
        else:
            raise IndexError("No item To delete")
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("No item Tat front")
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("No item Tat front")
    def size(self):
        return len(self)
    
d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
d1.delete_front()
d1.delete_rear()
print("Front :",d1.get_front(),"Rear :",d1.get_rear())
print("Size :",d1.size())