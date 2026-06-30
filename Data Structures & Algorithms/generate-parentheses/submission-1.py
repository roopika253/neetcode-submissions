class Solution:
    def helper(self, n, temp, l, r):
       
        if l == n and r == n:
            self.ans.append(temp[:])
            return
        
        if l < n:
            self.helper(n, temp +"(", l+1 , r)

        if r < l:
            self.helper(n, temp + ")", l , r+1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.helper(n,"" , 0 , 0)
        return self.ans

        