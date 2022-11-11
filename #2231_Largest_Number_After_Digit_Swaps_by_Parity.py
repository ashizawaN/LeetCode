class Solution:
    def largestInteger(self, num: int) -> int:
        nums = [int(i) for i in str(num)]
        even, odd = [], []

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        even.sort()
        odd.sort()

        rec = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                rec = rec*10 + even.pop()
            else:
                rec = rec*10 + odd.pop()
        return rec
