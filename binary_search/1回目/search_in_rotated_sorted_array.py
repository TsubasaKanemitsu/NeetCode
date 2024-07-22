from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 初回解答
        # l, r = 0, len(nums) - 1
        # min_val = min(nums[l], nums[r])
        
        # while r - l > 1:
        #     m = (l + r) // 2
        #     min_val = min(min_val, nums[m])

        #     if nums[m] <= nums[r]:
        #         r = m
        #     else:
        #         l = m

        # min_val_idx = r
        # if min_val > target:
        #     return -1
    
        # if nums[len(nums) - 1] >= nums[0]:
        #     l, r = 0, len(nums) - 1
        # else:
        #     if target <= nums[len(nums) - 1]:
        #         l, r = min_val_idx, len(nums) - 1
        #     else:
        #         l, r = 0, min_val_idx - 1

        # while l <= r:
        #     m = (l + r) // 2
        #     if nums[m] > target:
        #         r = m - 1
        #     elif nums[m] < target:
        #         l = m + 1
        #     else:
        #         return m
        # return -1

        # 別解
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            if nums[m] == target:
                return m

            if nums[m] < nums[r]:
                if target < nums[m] or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

        return -1

s = Solution()
# nums = [3,4,5,6,1,2]
# target = 1

# nums = [3,5,6,0,1,2]
# target = 4

# nums = [1]
# target = 1

# nums = [1, 2, 3, 4, 5, 6]
# target = 1

print(s.search(nums=nums, target=target))