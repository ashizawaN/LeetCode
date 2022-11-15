# time complexity: O(n)
# space complexity: O(logn)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def rec(node: Optional[TreeNode], sum_num: int) -> int:
            if not node:
                return sum_num

            node.val += rec(node.right, sum_num)
            return rec(node.left, node.val)

        rec(root, 0)
        return root
