class Node:
    def __init__(self, element, nxt = None):
        self._element = element
        self._nxt = nxt
    
    def __str__(self):
        return()

    def getElement(self):
        return self._element

    def getNxt(self):
        return self._nxt

    def setElement(self, e):
        self._element = e

    def setNxt(self, n):   
        if not isinstance(n, Node):
            raise TypeError("Nxt must be set to a Node")
        self._nxt = n
    
def push(node):
    global head
    node.setNxt = head
    node, head = head, node
    

if __name__ == '__main__':
    head = Node('LAX')
    n1 = Node('MSP')
    head.setNxt(n1)
    n2 = Node('ATL')
    n1.setNxt(n2)
    i = head
    n4 = push(Node('BOS'))