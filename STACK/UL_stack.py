class Stack:
    def __init__(self) -> None:
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    
    def push(self,data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            print("The Last Element is :",self.items[-1])
        else:
            raise IndexError("Stack is empty")

    def size(self):
        print("Elements Present is :",len(self.items))

s1=Stack()
s1.push(0)
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)
s1.push(7)
s1.size()
print("Removed Element is :",s1.pop())
s1.peek()
s1.size()