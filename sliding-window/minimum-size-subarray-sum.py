class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums)==0:
            return 0
        left=0
        result= len(nums)+1
        sum=0
        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                result=min(result,right-left+1)
                sum-=nums[left]
                left+=1
        if result==len(nums)+1:
            return 0
        return result
            
        