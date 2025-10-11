class Solution: #（的数量要>=),不然出错
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtracking(n,result,left,right,str):
            if left<right: #dang (<<<<)
                return
            if left==right==n:
                result.append(str)
                return 
            if left<n:#当(小于n.  加左边括号
                backtracking(n,result,left+1,right,str+"(")
            if right<left:  # 只有左括号(更多时，才能放右括号)
                backtracking(n,result,left,right+1,str+")")
        backtracking(n,result,0,0,"")
        return result
        