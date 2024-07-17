class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # l_array = [1] * length
        # r_array = [1] * length
        output = [1] * length
        for i in range(1, length):
            output[i] = output[i-1] * nums[i-1]
        right = nums[-1]
        for i in range(length-2, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output