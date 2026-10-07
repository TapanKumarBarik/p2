class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        final_arr=[]
        nums.sort()

        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            
            for j in range(i+1,n-2):

                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                # now we have a and b lets find c and d 

                left =j+1
                right = n-1
                while left<right:
                    temp = nums[i]+nums[j]+nums[left]+nums[right]
                    if temp>target:
                        right-=1
                    elif temp<target:
                        left+=1
                    else:
                        res=[nums[i],nums[j],nums[left],nums[right]]
                        final_arr.append(res)

                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]== nums[right-1]:
                            right-=1
                        
                        left+=1
                        right-=1
            
        
        return final_arr


s = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
result = s.fourSum(nums, target)
print(result)