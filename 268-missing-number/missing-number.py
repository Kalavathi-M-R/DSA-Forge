class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        total = sum(nums)
        n = len(nums)
        return int(abs((n*(n+1)/2)-total))
        