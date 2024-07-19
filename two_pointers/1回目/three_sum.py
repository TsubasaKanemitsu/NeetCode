from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 誤り
        # l, r = 0, len(nums) - 1
        # nums = sorted(nums)
        # res = set()
        # while r - l > 1:
        #     if nums[l] + nums[r] + nums[r - 1] == 0:
        #         res.add((nums[l], nums[r - 1], nums[r]))
        #     elif nums[l] + nums[r] + nums[l + 1] == 0:
        #         res.add((nums[l], nums[l + 1], nums[r]))
            
        #     if nums[l] + nums[r] < 0:
        #         l +=  1
        #     else:
        #         r -= 1
            
        # return [[i, j, k] for i, j, k in list(res)]

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if  a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0 :
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


nums=[3,0,-2,-1,1,2]
s = Solution()
print(s.threeSum(nums))