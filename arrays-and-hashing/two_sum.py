from typing import List

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             if i == j:
    #                 continue

    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[nums[i]] = i
                        
            

nums = list(map(int, input().split()))
target = int(input())

s = Solution()
print(s.twoSum(nums, target))