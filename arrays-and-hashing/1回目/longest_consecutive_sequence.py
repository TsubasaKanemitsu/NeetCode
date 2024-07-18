from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        max_cnt = 0
        for i in range(len(nums)):
            # 開始位置であるかをチェック
            if nums[i] - 1 not in numSet:
                cnt = 1
                while nums[i] + cnt in numSet:
                    cnt += 1
                max_cnt = max(max_cnt, cnt)
        
        return max_cnt
    
s = Solution()
print(s.longestConsecutive(nums))