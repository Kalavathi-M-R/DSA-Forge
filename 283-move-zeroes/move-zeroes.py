class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        count_zeros = 0
        for num in nums:
            if num!=0:
                temp.append(num)
            else:
                count_zeros+=1
        temp += ([0]*count_zeros)
        nums[:] = temp

        
        