class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #HashMap implementation:
        HashMap = {}

        for i in range(len(nums)):
            if nums[i] in HashMap:
                HashMap[nums[i]] = HashMap[nums[i]] + 1
                if HashMap[nums[i]]>1:
                    return True
            else:
                HashMap[nums[i]] = 1
                
        return False

        # Set Implementation: T: O(N) S: O(N)
        # HashSet = set()
        # for e in range(len(nums)):
        #     if nums[e] in HashSet:
        #         return True
        #     else:
        #         HashSet.add(nums[e])