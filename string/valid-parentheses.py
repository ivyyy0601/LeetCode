class Solution:
    #你在循环中每次都在修改 flag，但是如果最后一次括号刚好匹配上，就会让 flag=1，即使前面有不匹配的情况，也被覆盖掉. 用flase就行
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                else:
                    if char==')' and stack.pop()!='(':
                        return False
                    elif char==']' and stack.pop()!='[':
                        return False
                    elif char=='}' and stack.pop()!='{':
                        return False
        if len(stack)==0:
            return True
        else:
            return False

        