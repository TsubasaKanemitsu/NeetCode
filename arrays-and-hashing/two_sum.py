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
        for i in range(len(nums)):
            idx = hashMap.get(target - nums[i], -1)
            if idx == -1:
                hashMap[nums[i]] = i
                continue

            if i > idx:
                return list([idx, i])
            return list([i, idx])
            
            

nums = list(map(int, input().split()))
target = int(input())

s = Solution()
print(s.twoSum(nums, target))