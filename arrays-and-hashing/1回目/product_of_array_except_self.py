from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 愚直解
        # output = list()
        # for i in range(len(nums)):
        #     val = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         val *= nums[j]
        #     output.append(val)
        # return output

        # 高速化
        # res = [1 for _ in range(len(nums))]
        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums) - 1, - 1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]

        # 高速化（left, rightを用意する）
        left = [1]
        right = [1]
        for i in range(len(nums) - 1):
            left.append(nums[i]*left[i])
        for i in range(len(nums) - 1, 0, -1):
            right.append(nums[i]*right[len(nums) - 1 - i])

        res = []
        for i in range(len(nums)):
            res.append(left[i]*right[len(nums) - 1 - i])
            
        return res
    
nums = list(map(int, input().split()))
s = Solution()
print(s.productExceptSelf(nums))