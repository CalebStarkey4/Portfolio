from Empty import Empty
from collections import deque

class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self,cap=DEFAULT_CAPACITY):
    """Create an empty queue."""
    self._data = [None] * cap
    self._size = 0
    self._front = 0
    self._back = -1                                              # _back marks the logical back of the deque, for the purposes of keeping this accurate it is instantiated to -1

  def __str__(self):
    """Print contents of deque in logical order"""
    toString = [None] * self._size                              # allocate list with capacity to match size (since we know how much we'll need)
    walk = self._front
    for k in range(self._size):                                 # only consider existing elements
      toString[k] = self._data[walk]                            # intentionally shift indices
      walk = (1 + walk) % len(self._data)                       # use size of underlying array as modulus
    return str(self._data) + "\n" + str(toString)               # return self._data (linear order) and toString (logical order)  

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.
    Raise Empty exception if the queue is empty."""
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def last(self):
    """Return (but do not remove) the element at the back of the queue.
    Raise Empty exception if the queue is empty."""
    if self.is_empty():
      raise Empty('Queue is empty')
    return self.data[self._back]                                # returns the value at the logical back of the queue
    
  def delete_first(self):
    """Remove and return the first element of the queue (i.e., FIFO).
    Raise Empty exception if the queue is empty."""
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None                              # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1

    if 0 < self._size < len(self._data) // 4:
      self._resize(len(self._data) // 2)
    return answer

  def delete_last(self):
    """Remove and return the last element of the queue.
    Raise Empty exception if the queue is empty."""
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._back]                             # store the value at the logical end of the deque
    self._data[self._back] = None                               # help garbage collection
    self._back = (self._back - 1) % len(self._data)             # move _back to point to the new logical end of the deque
    self._size -= 1

    if 0 < self._size < len(self._data) // 4:
      self._resize(len(self._data) // 2)
    return answer

  def add_last(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self._data))                         # double the array size
    self._back = (self._back + 1) % len(self._data)             # move back so that it points to the next empty space after the logical end of the deque
    self._data[self._back] = e                                  # fill that empty space with the value e
    self._size += 1

  def add_first(self, e):
    """Add an element to the front of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self._data))                         # double the array size
    self._front = (self._front - 1) % len(self._data)
    self._data[self._front] = e
    self._size += 1

  def _resize(self, cap):                                       # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                                            # keep track of existing list
    self._data = [None] * cap                                   # allocate list with new capacity
    walk = self._front
    for k in range(self._size):                                 # only consider existing elements
      self._data[k] = old[walk]                                 # intentionally shift indices
      walk = (1 + walk) % len(old)                              # use old size as modulus
    self._front = 0                                             # front has been realigned
    self._back = self._size - 1                                 # back has been realigned

if __name__ == '__main__':
  D=ArrayQueue()
  print('#add A, B, C to back')
  D.add_last('A'); print(D,'\n')
  D.add_last('B'); print(D,'\n')
  D.add_last('C'); print(D,'\n')
  
  print('#remove from front')
  print(D.delete_first()); print(D,'\n')

  print('#add 1 to front, goes in slot vacated by A')
  D.add_first(1); print(D,'\n')

  print('#add 2 to front, wraps around')
  D.add_first(2); print(D,'\n')
 
  print('#remove from back')
  print(D.delete_last()); print(D,'\n')
  
  print('#fill up queue at back')
  for i in range(7): 
    D.add_last(chr(i+68))
  print(D,'\n')
  
  print('#add 3 to front, should double queue and add at end')
  D.add_first(3); print(D,'\n')

  print('remove from back until shrinks')
  for i in range(7): 
    print(D.delete_last()) 
    print(D,'\n')

  print('add to front until doubles')
  for i in range(7): 
    D.add_first(i+4); 
  print(D,'\n')

  print('empty out queue, alternating front/back')
  while not D.is_empty():
    if len(D) % 2:
      print(D.delete_first())
    else:
      print(D.delete_last())
    print(D,'\n')

  print('trying to view (last) element in empty queue causes exception')
  print(D.last())   