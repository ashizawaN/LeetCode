# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_sum = 0
        nums.sort()
        i = 0
        j = len(nums)-1
        while i < j:
            max_sum = max(max_sum, nums[i]+nums[j])
            i += 1
            j -= 1
        return max_sum
