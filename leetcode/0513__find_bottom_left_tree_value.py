from typing import Optional
from collections import deque


"""
Given the root of a binary tree, return the leftmost value in the last row of
the tree.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        >>> s = Solution()
        >>> root = TreeNode(1)
        >>> s.findBottomLeftValue(root)
        1
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> s.findBottomLeftValue(root)
        2
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(3)
        >>> root.right.left = TreeNode(4)
        >>> root.right.right = TreeNode(5)
        >>> s.findBottomLeftValue(root)
        4
        """
        # return self.findBottomLeftValueLevelOrderTraversal(root)
        return self.findBottomLeftValueReverseLevelOrderTraversal(root)

    """
    Discussion: Initial thinking is to use level order tree traversal to
    systematically go to each row, noting the leftmost value for the current
    row being explored. If there are no more rows, then return the leftmost value.

    How will we know the level? Store with each node the level of the node. When
    we pop the node off the queue to process, we push its children into the node
    with level+1.

    Time:
    - n = number of nodes
    - => O(n) need to explore all nodes once

    Space:
    - n = number of nodes
    - => O(n) for space for the queue to store nodes to process
    """
    def findBottomLeftValueLevelOrderTraversal(self, root: Optional[TreeNode]) -> int:
        # create a list to use as a queue of nodes to explore, starting at
        # the root
        nodes = deque()
        nodes.append([root, 0])

        leftmostNode = None
        leftmostLevel = None

        # while we have nodes to explore, make note of leftmost one
        while len(nodes) > 0:
            (node, level) = nodes.popleft()
            if leftmostNode is None:
                leftmostNode = node
                leftmostLevel = level
            elif level > leftmostLevel:
                leftmostNode = node
                leftmostLevel = level
            if node.left is not None:
                nodes.append([node.left, level + 1])
            if node.right is not None:
                nodes.append([node.right, level + 1])
        return leftmostNode.val

    def findBottomLeftValueReverseLevelOrderTraversal(self, root: Optional[TreeNode]) -> int:
        """
        Discussion: Apparently we can optimize the above and not have
        to keep track of the current level by doing level order traversal
        but adding nodes into the queue in reverse order, so we process
        the nodes at each level from right to left instead of left to
        right. The last node should be the leftmost node at the lowest
        level.

        Time:
        - => O(n) again since we process each node once

        Space:
        - => O(n) again for queue storage
        """
        nodes = deque()
        nodes.append(root)

        curNode = None

        while len(nodes) > 0:
            curNode = nodes.popleft()
            if curNode.right is not None:
                nodes.append(curNode.right)
            if curNode.left is not None:
                nodes.append(curNode.left)
        return curNode.val

if __name__ == '__main__':
    import doctest
    doctest.testmod()
