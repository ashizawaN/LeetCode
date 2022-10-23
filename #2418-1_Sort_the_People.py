from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(heights)):
            x_names = names[i]
            x_heights = heights[i]
            j = i - 1
            
            while j>=0 and heights[j]<x_heights:
                names[j+1], heights[j+1] = names[j], heights[j]
                j -= 1
            names[j+1] = x_names
            heights[j+1] = x_heights
            
        return names
