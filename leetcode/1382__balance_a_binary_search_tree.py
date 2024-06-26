from typing import Optional
import TreeNode

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.balanceBST1(root)

    def balanceBST1(self, root: TreeNode) -> TreeNode:
        """
        Discussion:
        - A balanced binary search tree should have depth of at most floor(lg(n))
        - We can read all values of the BST into an array/list, and then
          insert the values into a new BST, balancing as we go

        Time: O(n) (read BST inorder)
        Space: O(n) (store values of BST in array)
        """
        values = self.readBST(root)
        result = self.buildBST(values)
        return result

    def readBST(self, root: TreeNode) -> list[int]:
        """
        Read the BST with the specified root node inorder, to get sorted list of values
        """
        values = []
        self.readBSTInorderRecur(root, values)
        return values

    def readBSTInorderRecur(self, node: Optional[TreeNode], values: list[int]) -> None:
        """
        Recursive (binary search) tree inorder traversal:
        - traverse left subtree
        - do something with current node
        - traverse right substree
        """
        if node is not None:
            self.readBSTInorderRecur(node.left, values)
            values.append(node.val)
            self.readBSTInorderRecur(node.right, values)

    def buildBST(self, values: list[int]) -> Optional[TreeNode]:
        """
        Builds a BST from a sorted list of (integer) values
        """
        if not values:
            return None

        mid = len(values) // 2
        root = TreeNode(values[mid])
        root.left = self.buildBST(values[:mid])
        root.right = self.buildBST(values[mid + 1:])
        return root

if __name__ == '__main__':
    import doctest
    doctest.testmod()
