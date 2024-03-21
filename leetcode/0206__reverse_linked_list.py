from typing import List, Optional

"""
Given the head of a singly linked list, reverse the list, and return the
reversed list.

Example 1:

Input: head = [1,2,3,4,5]

Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]

Output: [2,1]

Example 3:

Input: head = [] Output: []

Constraints:

* The number of nodes in the list is the range [0, 5000].  -5000 <= Node.val <=
* 5000

Follow up: A linked list can be reversed either iteratively or
recursively. Could you implement both?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mkLinkedList(values: list[int]) -> Optional[ListNode]:
    if values is None or len(values) == 0:
        return None
    nodes = []
    for val in values:
        n = ListNode(val)
        nodes.append(n)
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

def mkList(head: Optional[ListNode]) -> Optional[List[int]]:
    if head is None:
        return []
    values = []
    cur = head
    while cur is not None:
        values.append(cur.val)
        cur = cur.next
    return values

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        >>> s = Solution()
        >>> mkList(s.reverseList(mkLinkedList([1, 2, 3, 4, 5])))
        [5, 4, 3, 2, 1]
        >>> mkList(s.reverseList(mkLinkedList([1, 2])))
        [2, 1]
        >>> mkList(s.reverseList(mkLinkedList([])))
        []
        """
        return self.reverseListRecur(head)

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Read entire linked list into a list()
        2. Working backwards, link nodes
        3. Return tail node

        Time:
        - n = number of nodes starting from head
        - O(n) to traverse linked list and populate regular list
        - O(n) to traverse regular list and link nodes
        - => O(n)

        Space:
        - n = number of nodes starting from head
        - => O(n) regular list storage for nodes
        """
        if head is None:
            return None

        nodes = []
        n = head
        while n is not None:
            nodes.append(n)
            n = n.next
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i-1]
        nodes[0].next = None
        return nodes[-1]

    def reverseListIter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. Iteratively push nodes onto stack
        2. When at end, note head, and keep popping off nodes from stack, linking
        """
        if head is None:
            return None
        nodeStack = [] # use list as a stack
        cur = head
        while cur is not None:
            nodeStack.append(cur)
            cur = cur.next

        newHead = None
        
        while len(nodeStack) > 0:
            nextNode = nodeStack.pop()
            if newHead is None:
                newHead = nextNode
                cur = newHead
            else:
                cur.next = nextNode
                cur = cur.next
        cur.next = None
        return newHead

    def reverseListRecur(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive call version.
        1. Recursively call until we reach end of linked list
        2. When we've reached end of list, we keep returning that end node
           (which is now the new "head" node) and rearrange the current nodes
           (swap pointers between curNode and nextNode, then null out curNode's
           next pointer

        Time:
        - n = length of linked list
        - O(n) to traverse linked list recursively
        - O(1) at each step to rearrange node pointers
        - => O(n)

        Space:
        - n = length of linked list
        - => O(n) for the recursive call stack
        """
        if head is None:
            return None
        return self.reverseListRecurHelper(head)

    def reverseListRecurHelper(self, curNode: Optional[ListNode]):
        if curNode is None or curNode.next is None:
            # base case - current node is None, or is the last node
            return curNode
        else:
            # recursive step - recursively call this method to get basically the next
            # node, rearrange pointers
            #
            # Before:
            # [..., curNode, nextNode, ..., newHeadNode]
            #
            # After:
            # [newHeadNode, ..., nextNode, curNode, ...]
            #
            newHeadNode = self.reverseListRecurHelper(curNode.next)
            nextNode = curNode.next
            nextNode.next = curNode
            curNode.next = None
            return newHeadNode

if __name__ == '__main__':
    import doctest
    doctest.testmod()
