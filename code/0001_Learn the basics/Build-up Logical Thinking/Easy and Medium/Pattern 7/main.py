class Solution:
    def pattern7(self, n):
        for i in range(n):
            for j in range(2 * n - 1):
                if j < n - i - 1:
                    print(" ", end="")
                elif j > n + i - 1:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()

sol = Solution()
n_list = [5, 3, 70]
for n in n_list:
    print(f"Pattern for n={n}:")
    sol.pattern7(n)
    print()