from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 1, 1
        for i in range(1, len(nums)):
            if nums[right]==nums[right-1]:
                right+=1
            elif nums[right]!=nums[right-1]:
                nums[left] = nums[right]
                left+=1
                right+=1
        return left
    
solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(nums))

