from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = 0
        
        for num in nums:
            if count == 0:
                majority = num
            if majority == num:
                count += 1
            else:
                count -= 1
        return majority