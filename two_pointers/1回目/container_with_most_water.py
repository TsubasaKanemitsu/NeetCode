from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 愚直解
        # area = -1
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area = max(area, min(heights[i], heights[j]) * (j - i))
        # return area

        # 高速化
        res = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1           
        return res
s = Solution()
print(s.maxArea([1, 7, 2, 5, 4, 7, 3, 6]))