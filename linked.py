class node:
    def __init__(self,d):
        self.data=d
        self.addr=None
o1=node(500)
o2=node(300)
o3=node(400)
o2.addr=o3
o3.addr=o1
temp=o2
while temp:
    print(temp.data,"==>",end=' ')
    temp=temp.addr
    if(temp==None):
        print("NULL")
