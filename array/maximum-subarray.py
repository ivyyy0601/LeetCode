class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #用滑动窗口应该快一点：
        # #这是「最大子数组和」——用滑动窗不适合，因为没有固定窗口长度或固定“约束”，尤其有负数时，“该不该缩窗”没有统一判据。
        # left=0
        # res=0
        # for right in range(0,len(nums)):
        #     res=res+nums[right]
        #     if res+nums[left]<res:
        #         left+=1
        #         res=res-nums[left]
        # return res不行\U0001f645
        # cur = best = nums[0]
        # for x in nums[1:]: #从下标 1 开始，取到列表的最后一个元素。
        #     # 要么把当前数接在之前的和后面，要么从当前数重新开始
        #     cur = max(x, cur + x) #cur：以当前位置x为结尾的最大子数组和 累加  
        #     #若 cur + x 还不如 x 本身，说明之前那段拖后腿，从 x 重新开始。
        #     best = max(best, cur)  # best：全局最大值。
        # return best
#用divide & conquer的方法：
        def maxvalue(left,right):
            if left==right:
                return nums[left]
            mid=(left+right)//2
            left_max= maxvalue(left,mid)
            right_max=maxvalue(mid+1,right)
            cross_max=maxcross(left,right)
            return max(left_max,right_max,cross_max)
        def maxcross(left,right):
            mid=(left+right)//2
            max_left=nums[mid]
            left_sum=nums[mid]
            for left in range(mid-1,left-1,-1):
                left_sum=left_sum+nums[left]
                max_left=max(max_left,left_sum)
            max_right=nums[mid+1]
            right_sum=nums[mid+1]
            for right in range(mid+2,right+1):
                right_sum=right_sum+nums[right]
                max_right=max(max_right,right_sum)
            return max_right+max_left
        
        return maxvalue(0,len(nums)-1)
            