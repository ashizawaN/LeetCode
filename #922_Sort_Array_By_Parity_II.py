from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        L = len(nums)  
        
        while odd < L:                          
            if nums[odd] % 2 == 0:              
                nums[odd], nums[even] = nums[even], nums[odd]
                even += 2                         
            else:
                odd += 2                         
        return nums
