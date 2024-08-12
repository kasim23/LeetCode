from typing import List
class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l<=r:
            if nums[l]<target:
                l+=1
            elif nums[r]>target:
                r-=1
            elif nums[l]==nums[r]==target:
                return l
        return -1
    
solution = Solution()
nums = [-1,0,3,5,9,12]
nums2 = [-1,0,3,5,9,12]
print(solution.search(nums, target=9))
print(solution.search(nums2, target=2))