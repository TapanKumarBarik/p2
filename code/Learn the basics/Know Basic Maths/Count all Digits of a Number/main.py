class Solution:
    def countDigit(self, n):
        count = 1
        if n<10:
            return count
        while n>=10:
            count+=1
            n = n/10

        return count


s = Solution()
input_list = [1, 10, 100, 1000, 12345, 987654321]
for num in input_list:
    print(f"Number of digits in {num} is: {s.countDigit(num)}")