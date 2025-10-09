class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        flag=0
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            else:
                if len(stack)==0:
                    flag=0
                else:
                    if char==')' and stack.pop()=='(':
                        flag=1
                    elif char==']' and stack.pop()=='[':
                        flag=1
                    elif char=='}' and stack.pop()=='{':
                        flag=1
                    else:
                        flag=0
        if len(stack)==0 and flag==1:
            return True
        else:
            return False

        