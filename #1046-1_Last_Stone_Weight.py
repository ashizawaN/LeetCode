# time complexity: O(nlogn)
# space complexity: O(n)
import heapq
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

        for i, stone in enumerate(stones):
            stones[i] = -stone
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            if stone1 > stone2:
                heapq.heappush(stones, stone2 - stone1)
        return -heapq.heappop(stones) if len(stones) else 0
