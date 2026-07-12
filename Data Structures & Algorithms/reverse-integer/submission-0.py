class Solution:
    def reverse(self, x: int) -> int:
        isNegative = 0
        if x < 0:
            isNegative = 1
            x = x * (-1)
        ans = 0
       
        while x:
            r = x% 10
            x = x//10
            
            ans = ans*10 + r
        if -2 ** 31 <= ans <= 2**31 - 1:
            return ans * -1 if isNegative else ans
        return 0


        