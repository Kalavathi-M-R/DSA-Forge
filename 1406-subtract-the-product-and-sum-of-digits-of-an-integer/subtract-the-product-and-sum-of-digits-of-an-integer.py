class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        for digit in str(n):
            sum += int(digit)
            product *= int(digit)
        return (product - sum)
