class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = {}
        for i in s:
            if i in char_dict:
                char_dict[i]+=1
            else:
                char_dict[i] = 1
        for j in t:
            if j in char_dict:
                char_dict[j]-=1
            else:
                return False
        for count in char_dict.values():
            if count!=0:
                return False
        return True