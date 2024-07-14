from SLL import *

class Stack(SLL):
    def __init__(self) -> None:
        super().__init__()
        self.count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_first(data)
        self.count+=1
    def pop(self):
        if not self.is_empty():
            data = self.head.item
            self.delete_first()
            self.count-=1
            return data
        else:
            raise IndexError("Stack is empty!")
    def peek(self):
        if not self.is_empty():
            return self.head.item
        else:
            raise IndexError("Stack is empty!")
    def size(self):
        return self.count

    def insert_after(self, aft, data):
        raise AttributeError("No such Attribute exists in Stack")
    def insert_last(self, data):
        raise AttributeError("No such Attribute exists in Stack")
    def delete_item(self, data):
        raise AttributeError("No such Attribute exists in Stack") 
    def delete_last(self):
        raise AttributeError("No such Attribute exists in Stack")
    def search(self, data):
        raise AttributeError("No such Attribute exists in Stack")
    def printlist(self):
        raise AttributeError("No such Attribute exists in Stack")
        
        
        
        
    

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print("Removed Element is:",s1.pop())
print("Top element is:",s1.peek())
print("Length of Stack is:",s1.size())
