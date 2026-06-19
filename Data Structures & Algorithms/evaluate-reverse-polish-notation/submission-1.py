
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ["+","-","*","/"]
        for i in tokens:
            if i == "+":
                a = st.pop()
                b = st.pop()
                c = b + a
                st.append(c)
            elif i == "-":
                a = st.pop()
                b = st.pop()
                c = b - a
                st.append(c)
            elif i == "*":
                a = st.pop()
                b = st.pop()
                c = b * a
                st.append(c)
            elif i == "/":
                a = st.pop()
                b = st.pop()
                c = int(b/a)
                st.append(c)
            else :
                st.append(int(i))
        return st.pop()




        