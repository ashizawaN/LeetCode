# time complexity: O(n)
# space complexity: O(n)
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def rec(node: TreeNode, low: int, high: int) -> int:
            if not node:
                return high - low
            left = rec(node.left, low, node.val)
            right = rec(node.right, node.val, high)
            return min(left, right)
        return rec(root, float(-inf), float(inf))
