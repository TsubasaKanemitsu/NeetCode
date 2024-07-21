from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles) + 1
        res = high
        while low <= high:
            k = (low + high) // 2
            total_eat_time = sum([ceil(piles[i] / k) for i in range(len(piles))])
            if total_eat_time <= h:
                high = k - 1
                res = min(res, k)
            elif total_eat_time > h:
                low = k + 1
        return res
        
    
s = Solution()
# piles = [25,10,23,4]
# h = 4

# piles = [10]
# h = 9

piles=[30,11,23,4,20]
h=6

print(s.minEatingSpeed(piles=piles, h=h))