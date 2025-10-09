class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result=1
        count=1
        for r in range(0,len(nums)):
            l=r-1
            if nums[l] == 1 and nums[r] == 1:
                count+=1
                result= max(count,result)
            else:
                count=1
                continue
        return result
