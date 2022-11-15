# time complexity: O(n)
# space complexity: O(logn)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        node_val = {}
        freqency = 0

        def find_target(root):
            if not root:
                return
            if root.val in node_val:
                node_val[root.val] += 1
            else:
                node_val[root.val] = 1
            find_target(root.left)
            find_target(root.right)
            return

        find_target(root)
        node_val_list = list(node_val.values())
        freqency = max(node_val_list)
        for key, value in node_val.items():
            if value == freqency:
                lst.append(key)
        return lst
