import heapq
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i, val in enumerate(nums):
            if len(heap) == k:
                heapq.heappushpop(heap, (val, i))
            else:
                heapq.heappush(heap, (val, i))
        heap.sort(key=lambda x: x[1])
        ans = []
        for i in heap:
            ans.append(i[0])
        return ans
