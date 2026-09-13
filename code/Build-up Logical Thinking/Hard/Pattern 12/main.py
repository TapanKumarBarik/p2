class Solution:
    def pattern12(self, n):
        for i in range(n):
            for j in range(2*n):
                if j<n:
                    if j<=i: 
                        print(j+1 , end="")
                    else:
                        print(" ",end="")
                else:
                    if j<2*n-1-i:
                        print(" ",end="")
                    else:
                        print(2*n-j,end="")
            
            print()
            
s = Solution()
n_list = [5, 6, 7,8,9]
for n in n_list:
    print(f"Pattern for n={n}:")
    s.pattern12(n)
    print()