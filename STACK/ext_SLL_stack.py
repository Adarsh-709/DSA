from SLL import *
class Stack:
    def __init__(self) -> None:
        self.mylist=SLL()
        self.n=0

    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_first(data)
        self.n+=1
    def pop(self):
        if not self.is_empty():
            data = self.mylist.head.item
            self.n-=1
            self.mylist.delete_first()
            return data
        else:
            raise IndexError("Stack is empty!")
    def peek(self):
        if not self.is_empty():
            return self.mylist.head.item
        else:
            raise IndexError("Stack is empty!")
    def size(self):
        return self.n

s1=Stack()
s1.push(0)
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
print("Top Element is:",s1.peek())
print("Removed Element is:",s1.pop())
print("Removed Element is:",s1.pop())
print("Removed Element is:",s1.pop())
print("Length of Stack is:",s1.size())
print("Top Element is:",s1.peek())

