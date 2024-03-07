from typing import Optional

"""
Given the head of a singly linked list, return the middle node of the linked
list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: head = [1,2,3,4,5]

Output: [3,4,5]

Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]

Output: [4,5,6]

Explanation: Since the list has two middle nodes with values 3 and 4, we return
the second one.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mkList(values: list[int]) -> ListNode:
    head = None
    cur = None
    for val in values:
        node = ListNode(val)
        if head is None:
            head = node
            cur = node
        else:
            cur.next = node
            cur = cur.next
    return head

def printList(head: Optional[ListNode]):
    print('[', end='')
    cur = head
    while cur is not None:
        print(f"{cur.val}, ", end='')
        cur = cur.next
    print(']', end='')

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Two pointers - one that steps twice each round, one that steps once.

        Check at each step of the end node pointer whether we need to break.

        [1]
         m,e
        [1, 2]
         m, e
        [1, 2, 3]
            m, e
        [1, 2, 3, 4]
               m, e
        [1, 2, 3, 4, 5]
               m,    e
        [1, 2, 3, 4, 5, 6]
                  m ,   e

        Time:
        - Let n = number of nodes
        - => O(n) end pointer traverses the list once through

        Space:
        - Let n = number of nodes
        - => O(1) pointers to middle and end of our search

        >>> s = Solution()
        >>> printList(s.middleNode(mkList([1])))
        [1, ]
        >>> printList(s.middleNode(mkList([1, 2, 3, 4, 5])))
        [3, 4, 5, ]
        >>> printList(s.middleNode(mkList([1, 2, 3, 4, 5, 6])))
        [4, 5, 6, ]
        """

        # base case - only 1 node, so mid == head
        if head.next is None:
            return head

        midNode = head
        endNode = head.next

        while True:
            # since mid for even-numbered nodes should be the second "middle",
            # we should advance this first
            midNode = midNode.next
            if endNode.next is None:
                break
            else:
                # try to advance the end node twice, breaking any time we
                # encounter a next that is None
                endNode = endNode.next
                if endNode.next is None:
                    break
                else:
                    endNode = endNode.next
        return midNode

if __name__ == '__main__':
    import doctest
    doctest.testmod()
