# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        MIN_LENGTH = 1
        MAX_LENGTH = 30
        MIN_NUM = 1
        MAX_NUM = 1000

        if len(stones) < MIN_LENGTH or len(stones) > MAX_LENGTH:
            raise ValueError("The range of stones should be 1 or more and 30 or less.")
        for i in range(len(stones)):
            if stones[i] < MIN_NUM or stones[i] > MAX_NUM:
                raise ValueError("The value of score should be 1 or more and 1000 or less")
            if type(stones[i]) != "int":
                raise TypeError("The type of a value in nums should be an integer.")

        for i in range(len(stones)-1):
            stones.sort()
            temp = stones[-1] - stones[-2]
            stones[-2] = 0
            stones[-1] = temp
        return (stones[-1])
