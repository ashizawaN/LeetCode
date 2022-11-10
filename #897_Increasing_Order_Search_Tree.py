# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> TreeNode:
        def inorder(node: TreeNode) -> TreeNode:
            if not node:
                return None
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        vals = []
        inorder(root)
        tree = TreeNode(vals[0])
        tmp = tree
        for num in vals[1:]:
            tmp.right = TreeNode(num)
            tmp = tmp.right
        return tree
