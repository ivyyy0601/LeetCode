class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #扩展法：后面的值加到前面去
        result=[]
        result.append([])
        for num in nums:
            temp=[]
            for res in result:
                r=res[:]
                r.append(num)
                temp.append(r)
            for t in temp:
                result.append(t)
        return result