class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        res = []
        num = ''.join(str(digit) for digit in digits)
        num = int(num)+1
        for n in str(num):
            res.append(int(n))
        return res