class Solution:
    def pattern22(self, n):
        for i in range(2*n-1):
            for j in range(2*n-1):
                if i==0 or j==0 or i==2*n-2 or j==2*n-2:
                    print(n,end=" ")
                else:
                    print(n - min(i, j, 2*n-2-i, 2*n-2-j), end=" ")
            print()
        


s = Solution()
s_list =[5, 6, 9]
for n in s_list:
    s.pattern22(n)
    print()