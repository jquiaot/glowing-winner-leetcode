from typing import Optional
from collections import deque

"""
A binary tree is named Even-Odd if it meets the following conditions:

- The root of the binary tree is at level index 0, its children are at level
  index 1, their children are at level index 2, etc.
- For every even-indexed level, all nodes at the level have odd integer values
  in strictly increasing order (from left to right).
- For every odd-indexed level, all nodes at the level have even integer values
  in strictly decreasing order (from left to right).

Given the root of a binary tree, return true if the binary tree is Even-Odd,
otherwise return false.

Discussion:

Since we need to go level by level to verify the properties of a possible
even-odd tree, we will do level-order traversal of the tree.

We can use a queue to maintain a list of nodes to process level by level.
We can store with each node in the queue its level, so we know when we
switch to the next level and how to evaluate the level.

The root is level 0.

Time:
- n = numer of nodes
- => O(n) because we need to explore all nodes

Space:
- n = number of nodes
- => O(n) worse case to hold all nodes in queue
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        nodes = deque()
        nodes.append([root, 0])

        curLevel = -1
        curNode = None
        
        # while there are nodes to process...
        while len(nodes) > 0:
            # pop the leftmost node
            (node, level) = nodes.popleft()

            # constraint - nodes should have opposite even/odd of its level
            if (level % 2 == 0 and node.val % 2 == 0) or \
                (level % 2 == 1 and node.val % 2 == 1):
                return False

            # if we're at a new level, then save the first node
            # we're seeing for comparison with next; also save level
            if level > curLevel:
                curLevel = level
                curNode = node
            # compare node values according to rules
            else:
                # even - strictly increasing (odd) values
                if level % 2 == 0 and curNode.val >= node.val:
                    print(f"even level and {curNode.val} >= {node.val}")
                    return False
                # odd - strictly decreasing (even) values
                if level % 2 == 1 and curNode.val <= node.val:
                    print(f"odd level and {curNode.val} <= {node.val}")
                    return False

            # push children of node into queue
            if node.left is not None:
                nodes.append([node.left, level + 1])
            if node.right is not None:
                nodes.append([node.right, level + 1])

            curNode = node

        # if we get all the way over here, we've processed all nodes in tree
        # and all conditions held, so return True
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
