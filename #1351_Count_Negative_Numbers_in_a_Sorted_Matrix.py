from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:    
        def BinarySearch(num):
            left = 0
            right = len(num)
        
            while left <= right:
                m = (left+right) // 2
                if num[m] < 0:
                    right = m - 1
                elif num[m] > 0:
                    left = m + 1
                else:
                    return m
            return left
        
        count = 0
        for x in grid:
            count += BinarySearch(x)
        return count