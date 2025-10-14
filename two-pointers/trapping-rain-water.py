class Solution:
    def trap(self, height: List[int]) -> int:
#O(n)   前最大值 和后最大d 然后取最小值-当前height。建立了三个数组 不建立数组
        # n=len(height)
        # pre_max=[0]*n
        # pre_max[0]=height[0] #第一个
        # for i in range(1,n):
        #     pre_max[i]=max(pre_max[i-1],height[i])
        # suf_max=[0]*n
        # suf_max[-1]=height[-1] #最后一个 不是suf_max[0]
        # for i in range(n-2,-1,-1):
        #     suf_max[i]=max(suf_max[i+1],height[i]) #从后往前加
        # res=0 
        # for h,pre,suf in zip(height,pre_max,suf_max):
        #     res+=min(pre,suf)-h

        # return res
        #空间复杂度减少 但是不好理解
        n= len(height)
        result=0
        left=0
        right=n-1
        pre_max=0
        suf_max=0
        while left<right:
            pre_max=max(pre_max,height[left])
            suf_max=max(suf_max,height[right])
            if pre_max<suf_max: #前面最大值就是pre_max 
                result += pre_max-height[left]
                left+=1
            else:
                result+=suf_max-height[right]
                right-=1
        return result