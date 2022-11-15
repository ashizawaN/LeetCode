import heapq
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        MIN_SCORE = 0
        MAX_SCORE = 10**6
        MIN_LENGTH = 1
        MAX_LENGTH = 10**4

        if type(score) != list:
            raise TypeError("The type of score should be list.")
        for i in range(len(score)):
            if score[i] < MIN_SCORE or score[i] > MAX_SCORE:
                raise ValueError("The value of score should be 1 or more and 10**6 or less")
            if type(score[i]) != "int":
                raise TypeError("The type of a value in nums should be integer.")
        if len(score) < MIN_LENGTH or len(score) > MAX_LENGTH:
            raise ValueError("The range of score should be 1 or more and 10**4 or less.")

        heap = []
        array = [None] * len(score)
        r = 1
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for i, val in enumerate(score):
            heapq.heappush(heap, (-val, i))
        while len(heap) != 0:
            _, i = heapq.heappop(heap)
            if r <= 3:
                array[i] = rank[r-1]
            else:
                array[i] = str(r)
            r += 1
        return array
