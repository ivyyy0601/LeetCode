class Solution:
    def trap(self, height: List[int]) -> int:
#O(n)   前最大值 和后最大d 然后取最小值-当前height
        n=len(height)
        pre_max=[0]*n
        pre_max[0]=height[0] #第一个
        for i in range(1,n):
            pre_max[i]=max(pre_max[i-1],height[i])
        suf_max=[0]*n
        suf_max[-1]=height[-1] #最后一个 不是suf_max[0]
        for i in range(n-2,-1,-1):
            suf_max[i]=max(suf_max[i+1],height[i]) #从后往前加
        res=0 
        for h,pre,suf in zip(height,pre_max,suf_max):
            res+=min(pre,suf)-h

        return res