class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        res=0
        for i in range(len(nums)):
            if nums[i]!= 0:
                nums[res]=nums[i]
                res+=1 #这里已经加了不需要了
        for i in range(res,len(nums)):
            nums[i]=0
        