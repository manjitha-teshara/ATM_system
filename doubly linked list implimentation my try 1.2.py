class Node:
    def __init__(self,d,n=None,p=None):
         self.data=d
         self.next=n
         self.prev=p

    def get_next(self):
        return self.next

    def set_next(self,n):
        self.next=n

    def get_data(self):
        return self.data

    def set_data(self,d):
        self.data=d

    def get_prev(self):
        return self.prev

    def set_prev(self,p):
        self.prev=p

class DoublyLinkedLIst:

    def __init__(self,r=None):
        self.root=r
        self.size=0

    def Size(self):
        return self.size

    def add(self,item):
        new_node=Node(item,self.root)
        if self.root:
            self.root.set_prev(new_node)
        self.root=new_node
        self.size+=1
        return print("Added",item)

    def find(self,item):
        
        nd=self.root
        while nd:
            if nd.data==item:
                return print("find ",item)

            else:
                nd=nd.next
        return print("not find ",item)

    def delete(self,item):
        nd=self.root

        while nd:
            if nd.data==item:
                next=nd.get_next()
                prev=nd.get_prev()

                if next:
                    next.set_prev(prev)
                if prev:
                    prev.set_next(next)
                else:
                    self.root=nd
                self.size-=1
                return True
            else:
                nd=nd.get_next()
        return False
    
lin=DoublyLinkedLIst()
lin.add(3)
lin.add(34)
lin.add(34)
lin.add(21)
lin.add(21)
lin.add(3)
print(lin.Size())
lin.find(8)
lin.find(34)
lin.find(2)
lin.find(21)

    

        

        
