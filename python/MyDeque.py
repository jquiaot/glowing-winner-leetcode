"""
My naive implementation of a deque (double-ended queue), using internal
node structure and prev/next pointers.

Operations/API:

- append(val) - appends element at the back of the deque
- appendleft(val) - appends element at the front of the deque
- pop() - removes element at the back of the deque; raises IndexError if 
  deque is empty
- popleft() - removes element at the front of the deque; raises IndexError
  if deque is empty
- peek() - examines, but does not remove, element at the back of the deque
- peekleft() - examines, but does not remove, the element at the front of the
  deque
- size() - returns the size of the deque

Time analysis:
- append()/appendleft() - O(1)
- pop()/popleft() - O(1)
- peek()/peekleft() - O(1)
- size() - O(1)

A few other notes/TODOs:

1. Not threadsafe
2. TODO implement arbitrary insert (supported by Python deque to maintain some
   list-like behavior)
"""
class MyDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0

    def append(self, val):
        n = self.Node(val)
        if self.tail is None:
            self.head = n
        else:
            self.tail.nextNode = n
            n.prevNode = self.tail
        self.tail = n
        self.sz += 1

    def appendleft(self, val):
        n = self.Node(val)
        if self.head is None:
            self.tail = n
        else:
            self.head.prevNode = n
            n.nextNode = self.head
        self.head = n
        self.sz += 1

    def pop(self):
        if self.tail is None:
            raise IndexError("Empty deque")
        n = self.tail
        self.tail = self.tail.prevNode
        if self.tail is not None:
            self.tail.nextNode = None
        self.sz -= 1
        return n.val

    def popleft(self):
        if self.head is None:
            raise IndexError("Empty deque")
        n = self.head
        self.head = self.head.nextNode
        if self.head is not None:
            self.head.prevNode = None
        self.sz -= 1
        return n.val

    def peek(self):
        if self.tail is None:
            raise IndexError("Empty deque")
        return self.tail.val

    def peekleft(self):
        if self.head is None:
            raise IndexError("Empty deque")
        return self.head.val

    def size(self):
        return self.sz

    class Node:
        def __init__(self, val = None, prevNode = None, nextNode = None):
            self.val = val
            self.prevNode = prevNode
            self.nextNode = nextNode
