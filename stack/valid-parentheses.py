class Solution:
    #你在循环中每次都在修改 flag，但是如果最后一次括号刚好匹配上，就会让 flag=1，即使前面有不匹配的情况，也被覆盖掉. 用flase就行
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch == '(' or ch=='{' or ch=='[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                stack_ele=stack.pop()
                if stack_ele=='(' and ch !=')':
                    return False
                elif stack_ele=='{' and ch !='}':
                    return False
                elif stack_ele=='[' and ch !=']':
                    return False
        if stack:
            return False
        return True