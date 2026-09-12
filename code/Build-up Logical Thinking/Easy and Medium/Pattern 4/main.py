class Solution:
    def pattern4(self, n):
        for i in range(n):
            for j in range(i+1):
                print(i+1,end="")
            print()




sol = Solution()
n_list = [5, 3, 7]
for n in n_list:
    print(f"Pattern for n={n}:")
    sol.pattern4(n)
    print()