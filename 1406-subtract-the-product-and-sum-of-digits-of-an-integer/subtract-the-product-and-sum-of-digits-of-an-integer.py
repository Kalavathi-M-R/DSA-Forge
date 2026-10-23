class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_sum = 0
        product = 1
        for digit in str(n):
            digit = int(digit)
            digit_sum += digit
            product *= digit
        return (product - digit_sum)
