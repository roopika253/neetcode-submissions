class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        for i in digits:
            ans = ans*10 + i
        ans += 1
        ans_array = []
        while ans:
            r = ans%10
            ans_array.append(r)
            ans = ans//10
        return ans_array[::-1]

        