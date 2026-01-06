import math
from TreeNode import TreeNode, mkTree
from typing import Optional
from collections import defaultdict

"""
Given the root of a binary tree, the level of its root is 1, the level
of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of
nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,None,None]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.

So we return the level with the maximum sum which is level 2.

Example 2:

Input: root = [989,None,10250,98693,-89388,None,None,None,-32127]
Output: 2

Constraints:

- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5
"""
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        >>> s = Solution()
        >>> s.maxLevelSum(mkTree([1,7,0,7,-8,None,None]))
        2
        >>> s.maxLevelSum(mkTree([989, None,10250, None,None,98693,-89388, None,None,None,None,None,None,None,-32127]))
        2
        >>> s.maxLevelSum(mkTree([1,1,0,7,-8,-7,9]))
        1
        """
        return self.maxLevelSum1(root)

    """
    Depth-first traversal of tree, keeping track of sums by level.

    Time:
    - n = number of nodes
    - O(n) traversal
    - O(n) in the worst case to traverse through levels and their
      sums to find the max sums
    - => O(n)

    Space:
    - n = number of nodes
    - h = height of tree
    - O(h) stack storage
    - O(h) storage of depths and their sums
    - => O(h)
    - Would we be able to say O(lg(n)), since the height of a typical tree if lg(n)?
    """
    def maxLevelSum1(self, root: Optional[TreeNode]) -> int:
        depth_sum = defaultdict(int)
        if root is None:
            return 0
        stack = [(root,1)]
        while len(stack) > 0:
            (node, depth) = stack.pop()
            depth_sum[depth] = depth_sum[depth] + node.val
            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))

        max_sum = -math.inf
        max_indexes = []
        for index, total in depth_sum.items():
            if max_sum < total:
                max_sum = total
                max_indexes = [index]
            elif max_sum == total:
                max_indexes.append(index)
        return min(max_indexes)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# END
