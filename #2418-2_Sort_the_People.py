from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x = zip(heights, names)
        sort_x = sorted(x, reverse=True)
        _, names = zip(*sort_x)
        return names
