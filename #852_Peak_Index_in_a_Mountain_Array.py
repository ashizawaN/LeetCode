from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)

        while left <= right:
            mid = (left+right) // 2
            
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            elif arr[mid] < arr[mid - 1]:
                right = mid - 1
            else:
                return mid
            
        
