class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        for i in range(len(str(x))):
             rev = (rev*10)+(temp%10)
             temp //= 10
        if  (x==rev):
            return True
        else:
            return False
