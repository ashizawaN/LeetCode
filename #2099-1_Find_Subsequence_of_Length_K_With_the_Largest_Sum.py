from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sort_nums = sorted(nums)
        for i in range(len(nums)-k):
            nums.remove(sort_nums[i])
        return nums
