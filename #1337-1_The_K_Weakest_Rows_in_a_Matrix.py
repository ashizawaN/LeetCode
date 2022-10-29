from typing import List
import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        ans = []
        for col, row in enumerate(mat):
            x = (sum(row), col)
            heapq.heappush(heap, x)
        for col in range(k):
            row = heapq.heappop(heap)
            ans.append(row[1])
        return ans