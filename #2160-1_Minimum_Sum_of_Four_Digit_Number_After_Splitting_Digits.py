class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [int(i) for i in list(str(num))]
        
        for i in range(1, len(nums)):
            x = nums[i]
            j = i - 1
            
            while j >= 0 and nums[j] < x:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = x

        return nums[0] + nums[1] + nums[2]*10 + nums[3]*10
