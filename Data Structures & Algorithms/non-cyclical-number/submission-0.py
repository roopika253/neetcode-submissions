class Solution:
    def recursion(self,n):
        s = 0
        while n :
            r = n%10
            n = n//10
            s += r*r
        return s
            
    def isHappy(self, n: int) -> bool:
        visited = set()
        s = self.recursion(n)
        while True:
            if s == 1:
                return True
            elif s in visited :
                return False
            visited.add(s)
            s = self.recursion(s)