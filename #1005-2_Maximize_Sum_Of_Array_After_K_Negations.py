# time complexity: O(nlogn)
# space complexity: O(1)
import heapq
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])

        while k:
            num = heapq.heappop(heap)
            num = -num
            heapq.heappush(heap, num)
            k -= 1
        return sum(heap)
