class Solution:  
    def longestCommonPrefix(self, strs):
        #your code goes here 
        strs.sort()
        shortest  = lambda x: min(x, key=len)
        min_length = len(shortest (strs))
        n = len(strs)-1
        res =""
        print()
        for i in range(min_length):
            if strs[0][i] != strs[n][i]:
                return res 
            res +=strs[0][i]
        return res
    
    
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"])) # fl   
print(s.longestCommonPrefix(["dog","racecar","car"])) # ""