class Solution:
    def pattern13(self, n):
        #your code goes here
        num = 1
        for i in range(n):
            for j in range(i+1):
                print(num , end=" ")
                num+=1
            print()
            

s = Solution()
n_list = [5, 3, 4]
for n in n_list:
    print(f"Pattern for n={n}:")
    s.pattern13(n)
    print()