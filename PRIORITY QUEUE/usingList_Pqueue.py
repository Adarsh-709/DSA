class PriorityQueue:
    def __init__(self) -> None:
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
            
        self.items.insert(index,(data,priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty!")
        else:
            return self.items.pop(0)[0]

    def size(self):
        return len(self.items)
    
p=PriorityQueue()
p.push(10,3)
p.push(0,1)
p.push(20,10)
p.push(5,2)
p.push(30,13)
p.push(25,5)
p.push(40,3)
p.push(50,15)
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.size())