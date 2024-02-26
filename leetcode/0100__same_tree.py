from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return self.isSameTreeRecur(p, q)
        return self.isSameTreeIter(p, q)

    """
    Recursive solution -- check that current node is the same, and if so,
    recursively check for left and right subtrees.

    Time:
    - n = number of nodes
    - => O(n) to traverse all nodes in the tree for equality

    Space:
    - n = number of nodes
    - => O(lg(n)) if balanced, otherwise O(n)
    """    
    def isSameTreeRecur(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # conditions where the current nodes are the same:
        # - both are None
        # - both are not None and values are the same
        if p is None:
            return q is None
        elif q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTreeRecur(p.left, q.left) and self.isSameTreeRecur(p.right, q.right)

    """
    Iterative solution: Use a stack to help traverse the tree nodes in-order.

    Time:
    - n = number of nodes
    - => O(n) to check all nodes

    Space:
    - n = number of nodes
    - => O(n) worse case to push all nodes in stack
    """
    def isSameTreeIter(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            return q is None
        elif q is None:
            return False

        s1 = [p]
        s2 = [q]

        while len(s1) > 0 and len (s2) > 0:
            a = s1.pop()
            b = s2.pop()
            if a.val != b.val:
                return False
            if a.right is not None and b.right is not None:
                s1.append(a.right)
                s2.append(b.right)
            elif not (a.right is None and b.right is None):
                return False
            if a.left is not None and b.left is not None:
                s1.append(a.left)
                s2.append(b.left)
            elif not (a.left is None and b.left is None):
                return False
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
