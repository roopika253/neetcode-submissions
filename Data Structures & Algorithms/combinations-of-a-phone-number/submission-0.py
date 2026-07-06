class Solution:
    def helper(self, indx ,temp , dictionary , digits):
        if len(temp) == len(digits):
            self.ans.append(temp)
            return 
       
        for i in dictionary[int(digits[indx])]:
            self.helper(indx+1 ,temp + i , dictionary , digits)


    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_alphabet = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        if digits == "":
            return []
        self.ans = []
       
        self.helper(0,"",digits_to_alphabet , digits)
        
        return self.ans


        