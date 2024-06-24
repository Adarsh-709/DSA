                                         #CIRCULAR LINKED LIST

class Node:
    def __init__(self,item=None,next=None) -> None:
        self.item=item
        self.next=next

class CLL:
    def __init__(self,tail=None) -> None:
        self.tail=tail

    def is_empty(self):
        return self.tail==None
    
    def insert_at_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.tail=n
        else:
            n.next=self.tail.next
            self.tail.next=n

    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.tail=n
        else:
            n.next=self.tail.next
            self.tail.next=n
            self.tail=n

    def search(self,data):
        if self.is_empty():
            pass
        else:
            temp=self.tail
            while True:
                if temp.item==data:
                    return temp
                temp=temp.next

    def insert_after(self,aft,data):
        temp=self.search(aft)
        n=Node(data,temp.next)
        temp.next=n

    def printlist(self):
        if self.is_empty():
            print("The list is Empty!")
        else:
            temp=self.tail.next
            while temp!=self.tail:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item)

    def delete_first(self):
        if self.is_empty():
            pass
        else:
            self.tail.next=self.tail.next.next

    def delete_last(self):
        if self.is_empty():
            pass
        else:
            temp=self.tail.next
            while temp.next!=self.tail:
                temp=temp.next
            temp.next=self.tail.next
            self.tail=temp
    
    def delete_item(self,data):
        if self.is_empty():
            pass
        elif self.tail.item==data:
            self.delete_last()
        elif self.tail.next.item==data:
            self.delete_first()
        else:
            temp=self.tail.next
            while temp!=self.tail:
                if temp.next.item==data:
                    temp.next=temp.next.next
                temp=temp.next

    def __iter__(self):
        return CLLIterator(self.tail.next)

#CREATING ITERATOR FOR OUR LIST
class CLLIterator:
    def __init__(self,start,count=0) -> None:
        self.current=start
        self.start=start
        self.count=count
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        self.count=1
        return data

cll=CLL()
cll.insert_at_first(10)
cll.insert_at_first(5)
cll.insert_at_last(15)
cll.insert_at_last(20)
cll.insert_at_last(30)
cll.insert_at_last(35)
cll.insert_at_last(45)
cll.insert_at_last(55)
cll.insert_at_last(65)
cll.insert_at_last(70)
cll.insert_after(20,25)
cll.insert_after(35,40)
cll.insert_after(45,50)
cll.insert_after(55,60)
cll.printlist()
cll.delete_first()
cll.delete_item(15)
cll.delete_item(25)
cll.delete_item(35)
cll.delete_item(45)
cll.delete_item(55)
cll.delete_item(65)
cll.delete_last()

#PRINTING USING ITERATOR
for x in cll:
    print(x,end=" ")







