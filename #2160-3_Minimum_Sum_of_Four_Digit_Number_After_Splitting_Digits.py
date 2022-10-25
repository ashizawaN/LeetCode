from typing import List


class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [int(i) for i in list(str(num))]

        
        def merge_sort(arr: List[int]) -> int:
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            merge_l = merge_sort(left)
            merge_r = merge_sort(right)
            return merge(merge_l, merge_r)

        def merge(left: int, right: int) -> int:
            merged = []
            l_i, r_i = 0, 0
            while l_i < len(left) and r_i < len(right):
                if left[l_i] <= right[r_i]:
                    merged.append(left[l_i])
                    l_i += 1
                else:
                    merged.append(right[r_i])
                    r_i += 1
            if l_i < len(left):
                merged.extend(left[l_i:])
            if r_i < len(right):
                merged.extend(right[r_i:])
            return merged
        
        sort_nums = merge_sort(nums)    
        return sort_nums[0]*10 + sort_nums[1]*10 + sort_nums[2] + sort_nums[3]
