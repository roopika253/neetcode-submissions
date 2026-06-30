class Solution:
    def helper(self, n, temp, l, r):
        if l > n or r > n or l < r:
            return
        if l == n and r == n:
            self.ans.append(temp[:])
            return
        temp += "("
        self.helper(n, temp, l+1 , r)
        temp = temp[:-1]
        temp += ")"
        self.helper(n, temp, l , r+1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.helper(n,"" , 0 , 0)
        return self.ans

        