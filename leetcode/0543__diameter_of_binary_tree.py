from typing import Optional

"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Discussion:

The longest path between any two nodes in a tree should be the longest path on
some node's left and right children. So perhaps we can define some sort of
recursive function to calculate both the longest individual path from some node
to its child (i.e. node to furthest child), and also the longest path from
some node to its left and right children. We need the first to be able to detect
if we've found the longest overall path, we need the second to be able to tell
this node's parent what any longest single path would be starting at that node.
"""
class Solution:
    """
    >>> s = Solution()
    >>> s.diameterOfBinaryTree(None)
    0
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        (maxLen, maxDiam) = self.diameterOfBinaryTreeRecur(root)
        return maxDiam

    """
    Recursively determines the diameter of binary tree. Returns a tuple
    consisting of the maximum path length for either left or right child,
    as well as the maximum diameter discovered so far.

    - Base case: the specified node is None, so from this node, there are
      no paths to left or right children, so maxPathLen = 0 and maxDiam = 0
    - Recursive step: calculate the max path length and max diameter for left
      and right children. This node's max path length and max diameter is then
      the max path length down either child (plus 1 for this node). This node's
      max diameter then is either the max diameter discovered in either left
      or right child, or the sum of the max paths for this node's left
      and right children, whichever is greatest.

    Time:
    - Should be O(n) as we are checking the max diameter and max path lengths
      for each node in the tree

    Space:
    - For a balanced tree, should be O(lg(n)) to maintain the recursive stack
      calls
    """
    def diameterOfBinaryTreeRecur(self, node: Optional[TreeNode]) -> tuple[int, int]:
        if node is None:
            return [0, 0]
        left = self.diameterOfBinaryTreeRecur(node.left)
        right = self.diameterOfBinaryTreeRecur(node.right)
        maxDiam = 0
        if left[1] > maxDiam:
            maxDiam = left[1]
        if right[1] > maxDiam:
            maxDiam = right[1]
        if left[0] + right[0] > maxDiam:
            maxDiam = left[0] + right[0]
        return [max(left[0], right[0]) + 1, maxDiam]
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
