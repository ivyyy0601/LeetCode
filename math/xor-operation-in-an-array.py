class Solution(object):
    def xorOperation(self, n, start):
        # nums=[]
        # for i in range(n):
        #     nums.append(start + 2 * i)
        # result=  nums[0]  
        # for re in nums[1:]:
        #     result=re^result
        # return result
       # 题目里的 “Define an array” 只是数学上的定义，帮你理解公式，不是让你一定写出 nums = []。
        result=start
        for i in range(1,n):
            result=result^(start + 2 * i)
        return result
