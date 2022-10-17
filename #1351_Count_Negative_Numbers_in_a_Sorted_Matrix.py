from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:    
        def binary_search(num):
            left = 0
            right = len(num)
        
            while left < right:
                mid = (left+right) // 2
                if num[mid] < 0:
                    right = mid
                elif num[mid] >= 0:
                    left = mid + 1
            return len(num) - left
        
        count = 0
        for arr in grid:
            count += binary_search(arr)
        return count
    
    