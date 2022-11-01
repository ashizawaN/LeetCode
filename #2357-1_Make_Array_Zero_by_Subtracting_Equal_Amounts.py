from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        L = len(nums)
        count = 0
        while nums != [0]*L:
            min_num = min([num for num in nums if num > 0])
            for i in range(L):
                if nums[i] != 0:
                    nums[i] -= min_num
            count += 1
        return count
        