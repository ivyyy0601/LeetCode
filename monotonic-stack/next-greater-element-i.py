class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack=[]
        # result=[] 
        # for n2 in nums2:
        #     stack.append(n2)
        # for n1 in nums1:
        #     temp=[]
        #     found=0
        #     res=-1
        #     while len(stack)!=0 and found==0:
        #         top=stack.pop()
        #         temp.append(top)
        #         if top>n1:
        #             res=top#不需要比较的
        #         elif top==n1:
        #             found=1
        #     result.append(res)
        #     while len(temp)!=0:
        #         stack.append(temp.pop())
        # return result
        #用单调stack 很牛
        res=[]
        stack=[]
        mapping={}
        for num in nums2:
            while len(stack)!=0 and num>stack[-1]:
                temp=stack.pop()
                mapping[temp]=num
            stack.append(num)
        while len(stack) != 0:
            mapping[stack.pop()] = -1
        for num in nums1:
            res.append(mapping[num])

        return res
