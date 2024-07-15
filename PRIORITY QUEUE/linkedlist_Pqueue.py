class Node:
    def __init__(self,item=None,priority=None,next=None) -> None:
        self.item=item
        self.priority=priority
        self.next=next

class PriorityQueue:
    def __init__(self,start=None) -> None:
        self.start=start
        self.count=0

    def is_empty(self):
        return self.start==None
    
    def push(self,data,priority):
        if self.is_empty():
            n=Node(data,priority,self.start)
            self.start=n
        elif priority<self.start.priority:
            n=Node(data,priority,self.start)
            self.start=n
        else:
            temp=self.start
            while temp.next is not None and temp.next.priority<=priority:
                temp=temp.next
            n=Node(data,priority,temp.next)
            temp.next=n
        self.count+=1

    def pop(self):
        if not self.is_empty():
            temp=self.start.item
            self.start=self.start.next
            self.count-=1
            return temp
        else:
            raise IndexError("Priority Queue is empty!")
        
    def size(self):
        return self.count
        

p=PriorityQueue()
p.push(10,3)
p.push(1,2)
p.push(0,1)
p.push(3,3)
p.push(15,15)
p.push(2,3)

print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())
print(p.pop())