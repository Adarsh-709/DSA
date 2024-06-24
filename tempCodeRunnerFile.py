    temp=self.start
            while temp!=self.start.prev:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item,end=" ")