347. Top K Frequent Elements

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Approach:
1. Create a hashmap to store the frequency of each element in the array.
2. Iterate through the array nums and check if the element is in the hashmap, then increment value by 1.
3. If the element is not in the hashmap, then add it to the hashmap with value 1.
4. Extract the top k frequent values' keys from the hashmap.
5. Return the extracted keys.
6. To do this I used heapq. top_keys = heapq.nlargest(k, res_map, key=res_map.get)