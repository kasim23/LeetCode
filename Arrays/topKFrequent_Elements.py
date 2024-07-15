import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_map = {}
        for i in nums:
            if i in res_map:
                res_map[i]+=1
            else:
                res_map[i] = 1
        top_keys = heapq.nlargest(k, res_map, key=res_map.get)
        return top_keys