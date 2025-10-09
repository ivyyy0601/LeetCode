class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                else:
                    if char==')' and stack.pop()=='(':
                        return True
                    elif char==']' and stack.pop()=='[':
                        return True
                    elif char=='}' and stack.pop()=='{':
                        return True
                    else:
                        return False
            if len(stack)==0:
                return False

        