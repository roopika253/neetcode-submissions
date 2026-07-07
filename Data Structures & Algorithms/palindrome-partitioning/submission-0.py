class Solution:
    def helper(self,indx, n , tmp ,s):
        if indx >=n :
            self.ans.append(tmp[:])
           
            return
        for j in range(indx,n):
            pali = s[indx:j+1]
            if pali == pali[::-1]:
                tmp.append(pali)
                self.helper(j+1 ,n, tmp, s)
                tmp.pop()


    

    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.helper(0, len(s) , [] , s)
        return self.ans
    
        