from collections import deque
from typing import Optional

# Some useful utility methods since TreeNode seems to appear quite
# frequently in Leetcode problems.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
    def __repr__(self):
        return self.__str__()

def mkTree(vals: list[int]) -> Optional[TreeNode]:
    if vals is None or len(vals) == 0:
        return None

    nodes = deque()
    root = TreeNode(vals[0])
    nodes.append(root)
    i = 1
    while i < len(vals):
        node = nodes.popleft()

        leftVal = vals[i]
        if leftVal is not None:
            node.left = TreeNode(leftVal)
            nodes.append(node.left)
        else:
            # add None to nodes queue to hold space for a node that
            # doesn't exist (but is needed for level traversal to work);
            # yes I probably can account for this a bit more elegantly, maybe
            # consider refactoring this later
            nodes.append(None)
        i += 1
        if i < len(vals):
            rightVal = vals[i]
            if rightVal is not None:
                node.right = TreeNode(rightVal)
                nodes.append(node.right)
            else:
                nodes.append(None)
            i += 1
    return root

if __name__ == '__main__':
    print(mkTree(None))
    print(mkTree([]))
    print(mkTree([1]))
    print(mkTree([1, 2, 3]))
    print(mkTree([1, 2, 3, 4, 5, 6, 7]))
    print(mkTree([1, 2, 3, 4, None, None, 7]))
    print(mkTree([1, None, 2, None, None, None, 3]))
