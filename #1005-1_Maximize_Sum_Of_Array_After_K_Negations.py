# time complexity: O(n**2)
# space complexity: O(1)
import bisect
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(k):
            cal = nums[0]*-1
            nums.pop(0)
            bisect.insort_left(nums, cal)
        return sum(nums)
