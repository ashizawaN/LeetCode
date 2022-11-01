import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        k_weekest_rows = []
        for i, row in enumerate(mat):
            x = (sum(row), i)
            heapq.heappush(heap, x)
        for i in range(k):
            row = heapq.heappop(heap)
            k_weekest_rows.append(row[1])
        return k_weekest_rows