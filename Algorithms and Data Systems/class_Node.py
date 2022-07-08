class Node:
    
    def __init__(self,e):
        self.e = e
        self.next = None

    def get_e(self):
        return self.e

    def get_next(self):
        return self.next

    def set_e(self,e):
        self.e = e

    def set_next(self,next):
        self.next = next

def myprint(i):
    while i:
        print(i.get_e,end = ' ')
        i=i.get_next()
    print()

def mypush(newnode):
    global head
    newnode.set_next(head)
    head = newnode

def mypop():
    global head
    e = head.get_e
    head.set_e(None)
    head = head.get_next
    return e

def findlast(i):
    while i.get_next():
        i = i.get_next()
    return i

def add_last(i):
    findlast(head).set_next(i)
    
if __name__ == '__main__':
    head = Node(1)
    n2 = Node(2)
    head.set_next(n2)
    myprint(head)
    mypush(Node(3))
    myprint(head)
    mypush(Node(4))

    j=findlast(head)
    print(j.e)

    while head:
        print(mypop())
        myprint(head)

    newnode = Node('A')
    mypush(newnode)
    myprint(head)