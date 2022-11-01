from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(a: int, b: int , array: List[int]):
            i, j, k = 0, 0, 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    array[k] = a[i]
                    i += 1
                else:
                    array[k] = b[j]
                    j += 1
                k += 1
            array[k:] = a[i:] if i < len(a) else b[j:]
           
               
        def merge_sort(nums: List[int]):
            if len(nums) == 1:
                return nums
            else:
                mid = len(nums) // 2
                left = nums[:mid]
                right = nums[mid:]
                merge_sort(left)
                merge_sort(right)
                merge(left, right, nums)
        
        merge_sort(nums)
        return nums
