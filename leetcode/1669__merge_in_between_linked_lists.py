# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mkLinkedList(values: list[int]) -> ListNode:
    nodes = []
    for val in values:
        nodes.append(ListNode(val))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

def mkList(head: ListNode) -> list[int]:
    vals = []
    cur = head
    while cur is not None:
        vals.append(cur.val)
        cur = cur.next
    return vals

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        """
        Since list1 is a linked list, we can't just jump to the b+1 node, we need to traverse
        list1 and remember both the insertion point as well as the remainder point.

        Time:
        - n = len(list1)
        - m = len(list2)
        - => O(n + m) to traverse list1 to find the incision points, as well as traverse
        -    list2 to find its endpoint to potentially tack on the remainder of list1

        Space:
        - => O(1) to remember list1 insertion point, remainder point, and endpoint of list2

        >>> s = Solution()
        >>> mkList(s.mergeInBetween(mkLinkedList([10, 1, 13, 6, 9, 5]), 3, 4, mkLinkedList([1000000, 1000001, 1000002])))
        [10, 1, 13, 1000000, 1000001, 1000002, 5]
        >>> mkList(s.mergeInBetween(mkLinkedList([0,1,2,3,4,5,6]), 2, 5, mkLinkedList([1000000,1000001,1000002,1000003,1000004])))
        [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6]
        """
        p1 = list1
        for i in range(a - 1):
            p1 = p1.next
        # p1 should now point to the (a-1) node

        p2 = p1.next
        for i in range(b - a + 1):
            p2 = p2.next
        # p2 should now point to the (b+1) node

        q1 = list2
        while q1.next is not None:
            q1 = q1.next

        p1.next = list2
        q1.next = p2

        return list1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
