class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        result=[] 
        for n2 in nums2:
            stack.append(n2)
        for n1 in nums1:
            temp=[]
            found=0
            res=-1
            while len(stack)!=0 and found==0:
                top=stack.pop()
                temp.append(top)
                if top>n1:
                    res=top
                elif top==n1:
                    found=1
            result.append(res)
            while len(temp)!=0:
                stack.append(temp.pop())
        return result
