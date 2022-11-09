from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        MIN_NUM = 1
        MAX_NUM = 10**3
        MIN_LENGTH = 2
        MAX_LENGTH = 500
        assert type(nums) == list, "The type of nums should be list."
        for i in range(len(nums)-1):
            if nums[i] < MIN_NUM or nums[i] > MAX_NUM:
                raise ValueError("The value of nums shoud be 1 or more and 10**3 or less.")
            if type(nums[i]) != "int":
                raise TypeError("The type of a value in nums should be integer.")
        if len(nums) < MIN_LENGTH or len(nums) > MAX_LENGTH:
            raise ValueError("The range of nums should be 2 or more and 500 or less.")

        largest_num = max(nums)
        nums.remove(largest_num)
        second_largest_num = max(nums)
        return (largest_num-1) * (second_largest_num-1)
