class Solution:
    def pattern9(self, n):
        for i in range(n):
            print(" " * (n - i - 1) + "*" * (2 * i + 1))

        for i in range(n - 1, -1, -1):
            print(" " * (n - i - 1) + "*" * (2 * i + 1))