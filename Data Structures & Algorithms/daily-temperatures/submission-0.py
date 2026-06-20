class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        st = []
        p = 0
        for i in range(n):
            while st and temperatures[i] > st[-1][0]:
                t ,indx = st.pop()
                result[indx] = (i-indx)
            st.append((temperatures[i],i))
        return result
            



        