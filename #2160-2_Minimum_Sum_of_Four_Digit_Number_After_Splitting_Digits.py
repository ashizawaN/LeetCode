class Solution:
    def minimumSum(self, num: int) -> int:
        sort_num = sorted(str(num))
        return int(sort_num[0])*10 + int(sort_num[1])*10 + int(sort_num[2]) + int(sort_num[3])
