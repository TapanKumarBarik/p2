class Solution:
    def NnumbersSum(self, N):
        #your code goes here
        if N==1:
            return N 
        return N+self.NnumbersSum(N-1)
    
    
s = Solution()
N_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for N in N_list:
    print(s.NnumbersSum(N))