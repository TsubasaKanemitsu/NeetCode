from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterNum = defaultdict(int)
        for n in nums:
            counterNum[n] += 1
        
        freq = [list() for _ in range(len(nums) + 1)]
        for v, cnt in counterNum.items():
            freq[cnt].append(v)

        res = list()
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

nums = list(map(int, input().split()))
k = int(input())
s = Solution()
print(s.topKFrequent(nums, k))