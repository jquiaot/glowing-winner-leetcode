from typing import Optional

"""
Given head, the head of a linked list, determine if the linked list has a cycle
in it.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is
used to denote the index of the node that tail's next pointer is connected
to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1

Output: true

Explanation: There is a cycle in the linked list, where the tail connects to
the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0

Output: true

Explanation: There is a cycle in the linked list, where the tail connects to
the 0th node.

Example 3:

Input: head = [1], pos = -1

Output: false

Explanation: There is no cycle in the linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Utility method for creating a linked list with a cycle. pos indicates
the node where the tail connects to. If pos == -1, there is no cycle.
"""
def createLinkedListWithCycle(values: list[int], pos: int) -> ListNode:
    # build an array of nodes, and link them later
    nodes = []
    for i in range(len(values)):
        nodes.append(ListNode(values[i]))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        >>> s = Solution()
        >>> s.hasCycle(createLinkedListWithCycle([3, 2, 0, -4], 1))
        True
        >>> s.hasCycle(createLinkedListWithCycle([1, 2], 0))
        True
        >>> s.hasCycle(createLinkedListWithCycle([1], -1))
        False
        """
        return self.hasCycle2(head)

    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        """
        If we can mutate the list, then what we can do is for each node in the list,
        change its next pointer to some constant value when we process it. If we
        find a node whos next pointer is our constant value, then we've found a cycle.
        We also terminate when we find a node whose next pointer is None.

        Time:
        - n = number of nodes
        - => O(n) traverse all nodes once (and one node possibly a second time to discover cycle)
        Space:
        - n = number of nodes
        => O(1) for dummy/sentinel node and curNode pointer
        """
        dummy = ListNode(-999999999)
        curNode = head
        while curNode is not None:
            if curNode.next == dummy:
                return True
            nextNode = curNode.next
            curNode.next = dummy
            curNode = nextNode
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        """
        If we cannot mutate list, we'll have to maintain other data structures to see
        if we can discover the cycle. Assuming ListNode is hashable, we can simply insert
        nodes as we encounter them into a set(),

        If we encounter a node with next pointer == None, then we're at end of list
        and there is no cycle.

        If we encounter a node with next pointer == a node already in set of seen nodes,
        there is a cycle.

        Time:
        - n = number of nodes
        - => O(n) we're still only traversing all nodes once, and one node at most
             twice to discover the cycle
        Space:
        - n = number of nodes
        - => O(n) to store nodes in a set for cycle detection
        """
        seen = set()
        curNode = head
        while curNode is not None:
            if curNode in seen:
                return True
            seen.add(curNode)
            curNode = curNode.next
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
