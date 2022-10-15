from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)

        while left <= right:
            m = (left + right) // 2
            
            if arr[m] < arr[m + 1]:
                left = m + 1
            elif arr[m] < arr[m - 1]:
                right = m - 1
            else:
                return m
            
        
