class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        result=[] 
        temp=[]
        found=0
        res=-1
        for n2 in nums2:
            stack.append(n2)
        for n1 in nums1:
            while len(stack)!=0 and found==0:
                top=stack.pop()
                if top>n1:
                    res=max(top,res)
                else:
                    found=1
                temp.append(top)
            result.append(res)
        while len(temp)!=0:
            stack.append(temp.pop())
        return result
