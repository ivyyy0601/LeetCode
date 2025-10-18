class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #你又几乎错误了！！！ 你是移一点对整体的product/sum进行改变
        if nums is None or len(nums)==0 or k<=1: #因为他说less than
            return 0
        ans=0
        left=0
        product=1
        for right in range(len(nums)) :
            product=nums[right]*product
            #while product<k and left<=right: #这里都是不符合的时候移动。之前那个是符合的时候移动
            #你在 prod < k 时不断收缩窗口，导致「合法」窗口被削短；
            while product>=k and left<=right:  #right=left的都是可以的  product=k
                product=product/nums[left] #要先运算 不然又忘记第一个.   # 先除，再移动 left
                left+=1  #因为left又走就会忘记之前的了
            ans+=right-left+1 
            #！！！不是简单相加，而是里面的全部满足    
            ## 以 right 结尾的合法子数组个数 子数组的   
            
        return ans
        