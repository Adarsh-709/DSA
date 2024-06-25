class Node:
    def __init__(self,item=None,next=None) -> None:
        self.item=item
        self.next=next
class Stack:
    def __init__(self) -> None:
        self.start=None
        self.item_count=0

    def is_empty(self):
        return self.start==None
    
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1
    
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError("Stack is empty!")
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty!")
    
    def size(self):
        return self.item_count

s1=Stack()
s1.push(0)
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
print("Top element is:",s1.peek())
print("Length of Stack is:",s1.size())
print("Removed element is:",s1.pop())
print("Top element is:",s1.peek())
print("Length of Stack is:",s1.size())
