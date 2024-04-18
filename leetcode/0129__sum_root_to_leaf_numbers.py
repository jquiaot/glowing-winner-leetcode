from typing import List, Optional
from TreeNode import TreeNode, mkTree

"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so
that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:

Input: root = [1,2,3]

Output: 25

Explanation:

The root-to-leaf path 1->2 represents the number 12.

The root-to-leaf path 1->3 represents the number 13.

Therefore, sum = 12 + 13 = 25.

Example 2:

Input: root = [4,9,0,5,1]

Output: 1026

Explanation:

The root-to-leaf path 4->9->5 represents the number 495.

The root-to-leaf path 4->9->1 represents the number 491.

The root-to-leaf path 4->0 represents the number 40.

Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:

* The number of nodes in the tree is in the range [1, 1000].

* 0 <= Node.val <= 9

* The depth of the tree will not exceed 10.
"""

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        >>> s = Solution()
        >>> s.sumNumbers(mkTree([1]))
        1
        >>> s.sumNumbers(mkTree([1, 2, 3]))
        25
        >>> s.sumNumbers(mkTree([4, 9, 0, 5, 1]))
        1026
        """
        return self.sumNumbersRecur(root)

    def sumNumbersRecur(self, root: Optional[TreeNode]) -> int:
        """
        Recursive implementation -- recursively traverse tree, depth-first,
        to generate the numbers from root to leaf. When a leaf is encountered,
        return the generated number. Intermediate nodes sum up and return
        numbers generated from leaves.

        Time:
        - n = number of nodes
        - O(n) to explore all nodes (depth-first traversal)
        - O((n+1)/2) numbers generated => O(n)
        - => O(n)

        Space:
        - n = number of nodes
        - O(lg(n)) depth of tree to explore
        - O(lg(n)) space for stack maintained in recursion
        """
        if root is None:
            return 0
        return self.sumNumbersRecurHelper(root, [root.val])

    def sumNumbersRecurHelper(self, node: Optional[TreeNode], curVal: list[int]) -> int:
        if node.left is None and node.right is None:
            return self.intDigitsToValue(curVal)
        else:
            totalSum = 0
            if node.left is not None:
                totalSum += self.sumNumbersRecurHelper(node.left, [*curVal, node.left.val])
            if node.right is not None:
                totalSum += self.sumNumbersRecurHelper(node.right, [*curVal, node.right.val])
            return totalSum

    def intDigitsToValue(self, digits: list[int]) -> int:
        value = 0
        for digit in digits:
            value *= 10
            value += digit
        return value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
