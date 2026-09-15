class Solution:
    def pattern19(self, n):
        for i in range(2*n):
            if i < n:
                print("*"*(n-i) + " "*(2*i) + "*"*(n-i))
            else:
                print("*"*(i-n+1) + " "*(2*(2*n-i-1)) + "*"*(i-n+1))
                
                
s = Solution()
n_list = [5, 6, 70]
for n in n_list:
    print(f"Pattern for n={n}:")
    s.pattern19(n)
    print()