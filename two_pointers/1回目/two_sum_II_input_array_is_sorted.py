from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 愚直解
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if target == numbers[i] + numbers[j]:
        #             return [i+1, j+1]
        
        # 高速化
        l = 0
        r = len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            else:
                return [l+1, r+1]
            


s = Solution()
print(s.twoSum([2, 7,11, 15], target=9))