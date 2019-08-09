class node:
    def __init__(self,d):
        self.data=d
        self.addr=None
class sll:
    def __init__(self):
        self.head=None
        
    def insert(self,d):
        temp=node(d)
        temp.addr=self.head
        self.head=temp
        
    def delete(self,d):
        temp=head
        self.head=temp.addr
        temp.addr=None
        
    def printlist(self,d):
        while(temp!=None):
            print(temp.data,"==>",end='')
            temp=temp.addr
        
obj=sll()
ch=0
while(ch!=4):
    print("1.insertion 2.deletion 3.print 4.exit")
    a=input()
    if (ch==1):
        obj.insert(a)
        obj.printlist()
    elif ch==2:
        obj.delete(a)
        obj.printlist()
    elif ch==3:
        obj.printlist()
    elif ch==4:
        exit(0)
    else:
        break
        
    
