class Solution:
    def reverseNumber(self, n):
        return int(str(n)[::-1])
    
    
s = Solution()
n_list = [123, 456, 789, 1000, 9876]
for n in n_list:
    print(s.reverseNumber(n))
    print("----------")