class Solution:    
    def palindromeCheck(self, s):
        #your code goes here

        n = len(s)-1

        i = 0
        while i<n:
            if s[i]!=s[n]:
                return False
            i+=1
            n-=1
        return True
    
    
s = Solution()
print(s.palindromeCheck("racecar")) # True
print(s.palindromeCheck("hello")) # False