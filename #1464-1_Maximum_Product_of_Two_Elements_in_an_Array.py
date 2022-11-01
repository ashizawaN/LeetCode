import heapq
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        count = 0
        MIN_NUM = 1
        MAX_NUM = 10**3
        MIN_LENGTH = 2
        MAX_LENGTH = 500
        assert type(nums) == list, "The type of nums should be list."
        for i in range(len(nums)-1):
            if type(nums[i]) != "int":
                count += 1
        if count == 0:
            assert "The type of a value in nums sould be integer."
        if len(nums) < MIN_LENGTH or len(nums) > MAX_LENGTH:
            raise ValueError("The range of nums should be 2 or more and 500 or less.")
        for i in range (len(nums)-1):
            if nums[i] < MIN_NUM or nums[i] > MAX_NUM:
                raise ValueError("The value of nums shoud be 1 or more and 10**3 or less.")
    
        heap = []
        for num in nums:
            if len(heap) <= 1:
                heapq.heappush(heap, num)
            else:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
        
        return (heapq.heappop(heap)-1) * (heapq.heappop(heap)-1)