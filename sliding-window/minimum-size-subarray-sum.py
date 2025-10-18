class Solution:
    #positive integers
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums)==0:
            return 0
        ans=len(nums)+1
        sum_res=0
        left=0
        for right in range(len(nums)):
            sum_res+=nums[right]
            while sum_res>=target:
                cur_len=right-left+1
                ans=min(cur_len,ans)
                sum_res-=nums[left] #顺序 是要先减掉他
                left+=1
                
                    
        if ans==len(nums)+1:
            return 0
        return ans

            
        