class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s1 = []
        for token in tokens: 
            if token in "+-*/":
                b = s1.pop()
                a = s1.pop()
                if token == "+":
                    result = a+b
                elif token == "-":
                    result = a-b
                elif token == "*":
                    result = a*b
                else:
                    result = int(a/b)
                s1.append(result)
            else:
               s1.append(int(token))
        return s1[-1]
