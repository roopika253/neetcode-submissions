class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        h1 = [0]*26
        h2 = [0]*26
        for i in s1:
            h1[ord(i)-97] += 1
      
        for i in range(m):
            h2[ord(s2[i])-97] += 1
        
        if h1 == h2:
            return True
        
        for i in range(m,n):
            h2[ord(s2[i])-97] += 1
            h2[ord(s2[i-m])-97] -= 1
            if h1 == h2:
                return True
           
        return False
        
        