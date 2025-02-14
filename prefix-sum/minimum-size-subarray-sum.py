class Solution(object):#滑动窗口
    def minSubArrayLen(self, target, nums):
        i=0
        j=0
        sum_re=0
        result=float('inf')
        for j in range(len(nums)):
            sum_re+=nums[j]
            while sum_re>=target :
                result=min(result,j-i+1)
                sum_re= sum_re - nums[i]
                i+=1
        if result==float('inf'):
            return 0
        else:
            return result
        # return result if result != float('inf') else 0 
                