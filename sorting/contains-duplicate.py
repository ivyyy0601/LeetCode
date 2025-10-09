class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dict={}
        # for n in nums:
        #     if n in dict:
        #         dict[n]+=1
        #     else:
        #         dict[n]=1
        # for value in dict.values():
        #     if value >1:
        #         return True
        # return False
        #用set快很多
        if nums is None or len(nums)==0:
            return False
        s=set(nums)
        return len(s) != len(nums)