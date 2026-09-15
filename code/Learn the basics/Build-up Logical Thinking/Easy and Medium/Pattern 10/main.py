class Solution:
    def pattern10(self, n):
        for i in range(2*n-1):
            if i<n:
                print("*"*(i+1) )
            else:
                print("*"*(2*n-i-1)  )



sol = Solution()
n_list = [5, 3, 70]
for n in n_list:
    print(f"Pattern for n={n}:")
    sol.pattern10(n)
    print()