class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, n in enumerate(nums):
            if n in hashmap and i - hashmap[nums[i]] <= k:
                return True
            hashmap[nums[i]] = i
        return False