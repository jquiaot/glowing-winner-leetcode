from typing import Optional, List
from TreeNode import TreeNode

"""
You are given the root of a binary tree where each node has a value in the
range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree
and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

- For example, "ab" is lexicographically smaller than "aba".

A leaf of a node is a node that has no children.

Example 1:

Input: root = [0,1,2,3,4,3,4]

Output: "dba"

Example 2:

Input: root = [25,1,3,1,3,0,2]

Output: "adz"

Example 3:

Input: root = [2,2,1,null,1,0,null,0]

Output: "abc"

Constraints:

- The number of nodes in the tree is in the range [1, 8500].

- 0 <= Node.val <= 25
"""
LETTERS = "abcdefghijklmnopqrstuvwxyz"
I2C = { i: LETTERS[i] for i in range(len(LETTERS)) }

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        return self.smallestFromLeafRecur(root, [root.val])
    
    def smallestFromLeafRecur(self, node: Optional[TreeNode], path: list[int]) -> str:
        """
        Strategery - generate leaf-to-root words, as they roll up, compare
        lexicographically with others, maintain the one that is smallest

        Time:
        - 
        Space:
        - 
        """
        if node.left is None and node.right is None:
            # leaf node, return its value
            return self.getWord(path)
        else:
            bestWord = None
            if node.left is not None:
                word = self.smallestFromLeafRecur(node.left, [*path, node.left.val])
                if bestWord is None or word < bestWord:
                    bestWord = word
            if node.right is not None:
                word = self.smallestFromLeafRecur(node.right, [*path, node.right.val])
                if bestWord is None or word < bestWord:
                    bestWord = word
            return bestWord

    def getWord(self, path: list[int]) -> str:
        # print(f"Getting word from {path}")
        return ''.join([I2C[x] for x in reversed(path)])

    def smallestFromLeafIter(self, root: Optional[TreeNode]) -> str:
        return ''
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
