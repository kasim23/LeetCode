217. Contains Duplicate
Problem Statement:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

Approach:
1. Use a Hashmap/dictionary to store the key value pairs. Key is the integer in the given array and value is the frequency of that integer in the original array.
2. Iterate through the array and check if the key is present in the hashmap/dictionary. If yes, then increment the value. If no, then value is 1.
3. If the value is greater than 1, then return true. Else return false.