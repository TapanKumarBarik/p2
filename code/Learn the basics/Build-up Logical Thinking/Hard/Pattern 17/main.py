class Solution:
    def pattern17(self, n):
        for i in range(n):
            num_to_add=0
            for j in range(2*n-1):
                
                if j<n:
                    #increasing
                    #n-i-1 space then A ++
                    if j<n-i-1:
                        print(" " ,end="")
                    else:
                        print(chr(ord("A")+num_to_add),end="")
                        num_to_add+=1
                else:
                    if j>=n+i:
                        break
                    else:
                        print(chr(ord("A")+n-j+i-1),end="")

            print()
            
            
s= Solution()
n_list=[5,6,7]
for n in n_list:
    print(f"Pattern for n={n}:")
    s.pattern17(n)
    print()