# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:        
        mid = len(nums) // 2
        nums.sort()
        i = 0
        j = mid
        if mid%2 != 0:
            j += 1
        max_num = 0
        while (i < mid):
            max_num += nums[i]
            if j < 2*mid:
                max_num += nums[j]
            i += 2
            j += 2
        return max_num
