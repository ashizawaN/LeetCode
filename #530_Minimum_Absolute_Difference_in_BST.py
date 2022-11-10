# time complexity: O(n)
# space complexity: O(logn)
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def rec(node: TreeNode, low: int, high: int) -> int:
            if not node:
                return high - low

            left = rec(node.left, low, node.val)
            right = rec(node.right, node.val, high)
            return min(left, right)

        return rec(root, -inf, inf)
