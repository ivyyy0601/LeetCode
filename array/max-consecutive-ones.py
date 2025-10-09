class Solution:
    #不用sliding windows
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result=0
        count=0
        if nums is None or len(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                result= max(result,count)
                count=0
        return max(result,count)