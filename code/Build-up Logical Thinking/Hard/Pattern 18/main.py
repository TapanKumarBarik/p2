class Solution:
    def pattern18(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(ord("A")+n-i+j-1),end=" ")
            print()



s= Solution()
n_list=[5,6,7]
for n in n_list:
    print(f"Pattern for n={n}:")
    s.pattern18(n)
    print()