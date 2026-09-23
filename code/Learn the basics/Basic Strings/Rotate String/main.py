
# class Solution:    
#     def rotateString(self, s, goal):
#         #your code goes here
#         if len(s)!=len(goal):
#             return False
#         if s == goal:
#             return True
#         n = len(s)
#         for i in range(1,len(s)):
#             new_curr = s[i:n] + s[0:i]
#             if new_curr ==goal:
#                 return True
#         return False



class Solution:
    def rotateString(self, s, goal):
        return len(s) == len(goal) and goal in s + s
    


sol = Solution()
s = "abcde"
goal = "cdeab"
print(sol.rotateString(s, goal))