class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        

        for s1 in s:
            if s1 in "{[(":
                stack.append(s1)
            elif not stack:
                return False
            
            

            elif s1==')' and stack[-1]=='(' or s1=='}' and stack[-1]=='{' or s1==']' and stack[-1]=='[' :
                   stack.pop()
            else:
                return False
        if not stack:
              return True
        return False
