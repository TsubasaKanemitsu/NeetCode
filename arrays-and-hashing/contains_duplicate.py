from collections import defaultdict
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        
        for _, v in cnt.items():
            if v >= 2:
                return True
        
        return False

input = list(map(int, input().split()))
s = Solution()
print(s.hasDuplicate(input))