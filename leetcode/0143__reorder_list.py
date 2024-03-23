from typing import Optional, List

"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be
changed.

Example 1:

Input: head = [1,2,3,4]

Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]

Output: [1,5,2,4,3]

Constraints:

* The number of nodes in the list is in the range [1, 5 * 10^4].

* 1 <= Node.val <= 1000
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
        nodes.append(ListNode(val))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

def mkList(head: Optional[ListNode]) -> Optional[list[int]]:
    if head is None:
        return None
    values = []
    cur = head
    while cur is not None:
        values.append(cur.val)
        cur = cur.next
    return values

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        >>> s = Solution()
        >>> head = mkLinkedList([1, 2, 3, 4])
        >>> s.reorderList(head)
        >>> mkList(head)
        [1, 4, 2, 3]
        >>> head = mkLinkedList([1, 2, 3, 4, 5])
        >>> s.reorderList(head)
        >>> mkList(head)
        [1, 5, 2, 4, 3]
        """
        return self.reorderList1(head)

    def reorderList1(self, head: Optional[ListNode]) -> None:
        """
        Naive implementation: read entire linked list into a regular list,
        then reorder as per requirements.

        Time:
        - n = number of nodes in linked list
        - O(n) to read nodes into regular list
        - O(n) to reorder nodes according to requirements
        - => O(n)

        Space:
        - n = number of nodes in linked list
        - => O(n) node storage
        """
        nodes = []
        cur = head
        while cur is not None:
            nodes.append(cur)
            cur = cur.next

        i = 0
        j = len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next = None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
