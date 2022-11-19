# time complexity: O(n)
# space complexity: O(1)
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        MIN_L = 2
        MAX_L = 10**4
        MIN_VAL = 1
        MAX_VAL = 10**4

        if len(nums) < MIN_L or len(nums) > MAX_L:
            raise ValueError("The value of nums shoud be 2 or more and 10**4 or less.")
        for i in range(len(nums)):
            if nums[i] < MIN_VAL or nums[i] > MAX_VAL:
                raise ValueError("The value of nums shoud be 1 or more and 10**4 or less.")
            if type(nums[i]) != "int":
                raise TypeError("The type of nums should be integer.")

        L = len(nums)
        s = L*(L+1)//2
        miss = s - sum(set(nums))
        duplicate = sum(nums) + miss - s
        return [duplicate, miss]
