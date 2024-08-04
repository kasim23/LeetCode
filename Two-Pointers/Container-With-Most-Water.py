from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0
        while l<r:
            width = r - l
            current_area = min(height[l], height[r]) * width
            max_area = max(max_area, current_area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
    
solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))