class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty!")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty!")
    def size(self):
        return len(self)
    
    def insert(self, index, object):
        raise AttributeError("No Attribute 'insert' in Stack!")

s1=Stack()
s1.push(0)
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.pop()
print("Top element is:",s1.peek())
print("Length of Stack is:",s1.size())