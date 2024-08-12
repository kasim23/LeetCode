from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows*cols - 1
        while low<=high:
            mid = (low+high)//2
            mid_value = matrix[mid//cols][mid%cols]
            if mid_value<target:
                low = mid + 1
            elif mid_value>target:
                high = mid - 1
            else:
                return True
        return False

s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(s.searchMatrix(matrix, target=3))