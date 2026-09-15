class Solution:
    def pattern21(self, n):
        for i in range(n):
            if i==0 or i==n-1:
                print("*"*n)
            else:
                print("*"+" "*(n-2)+"*")
                
s = Solution()
n_list = [5, 6, 7]
for n in n_list:
    print(f"Pattern for n={n}:")
    s.pattern21(n)
    print()