from Empty import Empty
class LeakyStack:
  """LIFO Leaky Stack implementation using a singly linked list for storage and adding a fixed cap on length."""
  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage
    def __init__(self, element, next):      # initialize node's fields
      self._element = element               # reference to user's element
      self._next = next                     # reference to next node
  #------------------------------- stack methods -------------------------------
  def __iter__(self):
    """New iterator to overwrite the inherited iterator"""
    _cursor = self._head
    while _cursor is not None:
          yield _cursor._element
          _cursor = _cursor._next

  def __init__(self, cap = 10):
    """Create an empty stack."""
    self._head = None                       # reference to the head node
    self._size = 0                          # number of stack elements
    self._cap = cap

  def __len__(self):
    """Return the number of elements in the stack."""
    return self._size

  def is_empty(self):
    """Return True if the stack is empty."""
    return self._size == 0
    
  def push(self, e):
    """Add element e to the top of the stack and 'leak' an element from the bottom if the stack is at capacity."""
    self._head = self._Node(e, self._head)  # create and link a new node
    if self._size < self._cap:
        self._size += 1
    else:
        i = self._head
        p = None
        while i._next is not None:
            p = i
            i = i._next
        i._element = None
        p._next = None

  def top(self):
    """Return (but do not remove) the element at the top of the stack.
    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._head._element              # top of stack is at head of list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).
    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    answer = self._head._element
    new_head = self._head._next
    self._head._element = None
    self._head._next = None
    self._head = new_head           # bypass the former top node
    self._size -= 1
    return answer

  def reverse2(self, came_before = None):
    temp = self._head
    if self._head._next:
      self._head = self._head._next
      self.reverse2(temp)
    temp._next = came_before

def myprint(ll):
  for e in ll:
    print(e,end = ' ')
  print()

def reverse(ll):
  r = LeakyStack(len(ll))
  for e in range(len(ll)):
    r.push(ll.pop())
  return r



if __name__ == '__main__':  
    L=LeakyStack(5)
    for i in range(5):
        L.push(i)
    myprint(L)
    L.push(5)
    myprint(L)
    print(L.pop());print(L.pop())
    myprint(L)
    L.push(6);L.push(7);L.push(8)
    myprint(L)
    L.reverse2()
    myprint(L)
