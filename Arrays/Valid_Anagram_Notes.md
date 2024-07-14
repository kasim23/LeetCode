242. Valid Anagram

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Approach:
1. If length of the two strings is not equal then return false because then they can't be anagrams.
2. Create a Hashmap/dictionary.
3. Iterate through the string s and add the characters to the dictionary.
4. If a character is already present in the Map, increment the value. The character acts as Key and the frequency of the character acts as Value.
5. If it is not already present in the Map, set the value to 1.
6. Repeat the above process for string t but this time if character is present in the Map, decrement the value by 1, if not in Map, return False.
7. Check the values in the map, if it is not equal to 0 then return false because if the words were anagrams, then at the end of the process the incremented values would all be decremented and the count would be 0, in which case the function would return True.