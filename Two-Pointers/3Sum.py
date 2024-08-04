from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []

        for i in range(len(nums) - 2):
            # Skip duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i+1, len(nums) - 1
            while l<r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum == 0:
                    result.append([nums[i],nums[l], nums[r]])
                    l+=1
                    r-=1
                # Skip duplicate values for l and r
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif current_sum<0:
                    l+=1
                else:
                    r-=1
        return result

solution = Solution()
nums = [-1,0,1,2,-1,-4]
print(solution.threeSum(nums))