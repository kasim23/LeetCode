class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        left = 0
        right = len(s) - 1
        for i in range(len(s)):
            if s[left]!= s[right]:
                return False
            else:
                left+=1
                right-=1
        return True
    
# Create an instance of the Solution class
solution = Solution()

s = "A man, a plan, a canal: Panama"
    
print(solution.isPalindrome(s))
    