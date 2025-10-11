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
        cur = best = nums[0]
        for x in nums[1:]: #从下标 1 开始，取到列表的最后一个元素。
            # 要么把当前数接在之前的和后面，要么从当前数重新开始
            cur = max(x, cur + x) #cur：以当前位置x为结尾的最大子数组和 累加  
            #若 cur + x 还不如 x 本身，说明之前那段拖后腿，从 x 重新开始。
            best = max(best, cur)  # best：全局最大值。
        return best
