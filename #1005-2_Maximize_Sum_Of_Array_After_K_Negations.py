# time complexity: O(nlogn)
# space complexity: O(n)
import heapq
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k:
            num = heapq.heappop(nums)
            heapq.heappush(nums, -num)
            k -= 1
        return sum(nums)
