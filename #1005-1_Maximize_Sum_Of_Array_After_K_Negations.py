# time complexity: O(n**2)
# space complexity: O(1)
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(k):
            nums[0] *= -1
            nums.sort()
        return sum(nums)
