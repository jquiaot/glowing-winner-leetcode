import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import MyDeque

"""
Unit tests for MyDeque.py
"""

class TestMyDeque(unittest.TestCase):

    def testBasic(self):
        d = MyDeque.MyDeque()

        self.assertEqual(d.size(), 0)

        d.append(1)
        d.append(2)

        self.assertEqual(d.size(), 2)
        self.assertEqual(d.peek(), 2)
        self.assertEqual(d.peekleft(), 1)

        d.appendleft(3)

        self.assertEqual(d.size(), 3)
        self.assertEqual(d.peek(), 2)
        self.assertEqual(d.peekleft(), 3)

        self.assertEqual(d.pop(), 2)
        self.assertEqual(d.pop(), 1)
        self.assertEqual(d.pop(), 3)

        d.appendleft(3)
        d.appendleft(2)
        d.appendleft(1)

        self.assertEqual(d.size(), 3)

        self.assertEqual(d.popleft(), 1)
        self.assertEqual(d.popleft(), 2)
        self.assertEqual(d.popleft(), 3)

    @unittest.expectedFailure
    def testPopOnEmpty(self):
        d = MyDeque.MyDeque()
        d.pop()

    @unittest.expectedFailure
    def testPopLeftOnEmpty(self):
        d = MyDeque.MyDeque()
        d.popleft()

if __name__ == '__main__':
    unittest.main()
