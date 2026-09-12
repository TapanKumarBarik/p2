class Solution:
    def pattern6(self, n):
        for i in range(n,0,-1):
            for j in range(i):
                print(j+1,end="")
            print()
            
sol = Solution()
n_list = [5, 3, 7]
for n in n_list:
    print(f"Pattern for n={n}:")
    sol.pattern6(n)
    print()