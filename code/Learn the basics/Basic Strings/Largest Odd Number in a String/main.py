class Solution:  
    def largeOddNum(self, s: str) -> str:
        #your code goes here

        # first remove all zero
        # find first number
        # keep going end and marking the last odd 

        start_index =0
        end_index =0
        i = 0
        n =len(s)

        while i<n:
            if s[i]=='0':
                i+=1
            else:
                break
        
        if i == n:
            return ""
        #till i we have zeres 
        start_index =i

        while i<n:
            if int(s[i])%2!=0:
                end_index = i
            i+=1

        if end_index==0 and int(s[start_index])%2==0:
            return ""
        return s[start_index:end_index+1]
        
        
s = Solution()
print(s.largeOddNum("000123456789")) # 123456789
print(s.largeOddNum("0002468")) # ""
# edge cases
print(s.largeOddNum("0")) # ""
print(s.largeOddNum("1")) # "1"
print(s.largeOddNum("2")) # ""
