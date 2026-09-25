class Solution: 
    def reverseString(self, s):
        #your code goes here
        n = len(s)-1
        i = 0

        while i<n:
            s[i],s[n] = s[n],s[i]
            i+=1
            n-=1
        return s
    
    
s = Solution()
print(s.reverseString(["h","e","l","l","o"])) # ["o","
