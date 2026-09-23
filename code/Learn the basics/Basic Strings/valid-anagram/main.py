class Solution:    
    def anagramStrings(self, s, t):
        #your code goes here

        if len(s) != len(t):
            return False
        s_map={}
        for char in s:
            if char in s_map:
                s_map[char]+=1
            else:
                s_map[char]=1
        for char in t:
            if char not in s_map:
                return False
            else:
                s_map[char]-=1
                if s_map[char]==0:
                    del s_map[char]

        return len(s_map) == 0



sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.anagramStrings(s, t))



