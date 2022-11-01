from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        L = len(mat)
        rows = sorted(range(L), key=lambda i: mat[i])
        return [rows[i] for i in range(k)]