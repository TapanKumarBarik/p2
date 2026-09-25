class Solution:
    def pattern14(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(ord("A")+j),end=" ")
            print()
            
            
s = Solution()
n_list = [22,23,24,25,26]
for n in n_list:
    print(f"Pattern for n={n}:")
    s.pattern14(n)
    print()