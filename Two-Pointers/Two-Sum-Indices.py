from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        result = []
        
        while left<right:
            if numbers[left]+numbers[right]<target:
                left+=1
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                result.append(left+1)
                result.append(right+1)
                break
        return result

solution = Solution()

target = 9
numbers = [2,7,11,15]
print(solution.twoSum(numbers, target))
                
            
