class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        x = (sum(aliceSizes) - sum(bobSizes)) // 2
        
        for i in aliceSizes:
            if i- x in set(bobSizes):
                return [i,i-x]      
