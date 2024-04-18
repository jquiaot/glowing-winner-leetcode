from typing import Optional, List
from TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        Strategy: Use breadth-first (level) traversal to locate all nodes at
        the target length, and insert new nodes per the rules. Take care of the
        special cases where root is None and depth == 1.

        Time:
        - n = number of nodes
        - Traverse at most all the nodes - O(n)
        - Perform node insert at some level of nodes - O(1)
        - => O(n)

        Space:
        - n = number of nodes
        - => O(n) some subset of nodes held in queue to process (current row
             and next row of nodes)
        - Tighter bounds?
        """
        if root is None:
            return None
        elif depth == 1:
            newRoot = TreeNode(val, left = root)
            return newRoot
        else:
            # breadth-first (level) traversal using a queue
            q = deque()
            q.append([root, 1])
            # the depth of the nodes whose subtrees need to be modified
            targetDepth = depth - 1
            while len(q) > 0:
                (cur, nd) = q.popleft()
                if nd == targetDepth:
                    curLeft = cur.left
                    curRight = cur.right

                    newLeft = TreeNode(val)
                    cur.left = newLeft
                    newLeft.left = curLeft

                    newRight = TreeNode(val)
                    cur.right = newRight
                    newRight.right = curRight
                elif nd < targetDepth:
                    if cur.left is not None:
                        q.append([cur.left, nd + 1])
                    if cur.right is not None:
                        q.append([cur.right, nd + 1])
                elif nd > targetDepth:
                    # don't need to process any nodes greater than the target depth
                    break
            return root

if __name__ == '__main__':
    import doctest
    doctest.testmod()
