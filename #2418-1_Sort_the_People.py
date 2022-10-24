from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(heights)):
            x_name = names[i]
            x_height = heights[i]
            j = i - 1
            
            while j >= 0 and heights[j] < x_height:
                names[j+1], heights[j+1] = names[j], heights[j]
                j -= 1
            names[j+1] = x_name
            heights[j+1] = x_height
            
        return names
