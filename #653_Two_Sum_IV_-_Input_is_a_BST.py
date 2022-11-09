# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def rec(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if node.val in vals:
                return True
            vals[k - node.val] = True
            return rec(node.left) or rec(node.right)
        vals = {}
        return rec(root)
