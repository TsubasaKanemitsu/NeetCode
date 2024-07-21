from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = min(nums[l], nums[r])

        while r - l > 1:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m

        return res
        
s = Solution()
nums = [3, 4, 5, 6]
# nums = [4,5,0,1,2,3]
# nums = [4,5,6,7]

print(s.findMin(nums=nums))