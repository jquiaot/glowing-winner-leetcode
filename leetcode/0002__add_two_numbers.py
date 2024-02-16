from typing import Optional

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Strategy: Basically, step through each list in lockstep, adding the
        vals and keeping track of carryover.

        Time:
        - m = len(l1), n = len(l2)
        - => O(k) where k is MAX(m, n)

        Space:
        - => O(k) where k is MAX(m, n) for new list being created
        """
        head = None
        cur = None
        cur1 = l1
        cur2 = l2
        carry = False
        while cur1 is not None or cur2 is not None:
            tmp = 0
            # print(f"{cur1.val} + {cur2.val} + carry={carry}")
            if cur1 is not None:
                tmp += cur1.val
                cur1 = cur1.next
            if cur2 is not None:
                tmp += cur2.val
                cur2 = cur2.next
            if carry:
                tmp += 1
                carry = False
            if tmp >= 10:
                tmp %= 10
                carry = True
            newNode = ListNode(tmp)
            if cur is None:
                cur = newNode
                head = cur
            else:
                cur.next = newNode
                cur = cur.next
        if carry:
            newNode = ListNode(1)
            cur.next = newNode
            cur = cur.next
        return head

    def addTwoNumbersHelper(self, l1: list[int], l2: list[int]):
        """
        Helper method for the above, converts the two int lists into ListNode
        form and invokes addTwoNumbers()

        >>> s = Solution()
        >>> s.addTwoNumbersHelper([0], [0])
        [0]
        >>> s.addTwoNumbersHelper([2, 4, 3], [5, 6, 4])
        [7, 0, 8]
        >>> s.addTwoNumbersHelper([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
        [8, 9, 9, 9, 0, 0, 0, 1]
        """
        ln1 = self.listToListNode(l1)
        ln2 = self.listToListNode(l2)
        lnResult = self.addTwoNumbers(ln1, ln2)
        print(self.listNodeToList(lnResult))

    
    def listToListNode(self, l: list[int]) -> Optional[ListNode]:
        if l is None:
            return None
        head = None
        cur = None
        for i in l:
            newNode = ListNode(i)
            if cur is None:
                cur = newNode
                head = cur
            else:
                cur.next = newNode
                cur = cur.next
        return head

    def listNodeToList(self, ln: Optional[ListNode]) -> list[int]:
        l = []
        if ln is not None:
            cur = ln
            while cur is not None:
                l.append(cur.val)
                cur = cur.next
        return l

if __name__ == '__main__':
    import doctest
    doctest.testmod()

