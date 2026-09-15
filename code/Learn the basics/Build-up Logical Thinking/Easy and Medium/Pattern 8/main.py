class Solution:
    def pattern8(self, n):
        for i in range(n):
            for j in range(2 * n):
                if j < i:
                    print(" ", end="")
                elif j < 2 * n - i - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
            
sol = Solution()
n_list = [5, 3, 70]
for n in n_list:
    print(f"Pattern for n={n}:")
    sol.pattern8(n)
    print()