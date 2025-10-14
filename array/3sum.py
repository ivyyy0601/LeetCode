class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #类似双指针：！
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-2): #保留n-1和n-2两个元素
            target=nums[i]
            if i>=1 and target== nums[i-1]:
                continue
            #这里优化：
            if target+nums[i+1]+nums[i+2]>0: #因为已经排好序了！！+最小的两个
            #说明target+后面的再大的都是>0 无法=0，同时target也不需要再继续了，因为target只会越来越大 不可能=0
                break
            if target+nums[-1]+nums[-2]<0:  #+最大的两个
                continue #这个就不用下面的while 因为这个target+ 到最大的两个都是<0
                # 但是有可能是因为target太小了，所以我们继续遍历target 有可能最终>0
            left=i+1
            right=n-1
            
            while left<right:
                sum=target+nums[left]+nums[right]
                if sum< 0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    res.append([target,nums[left],nums[right]])
                    left+=1
                    right-=1
                    # # 跳过 相邻重复！！！！！！！！！！所以前面要sort！！！ 不补上
                    while nums[left]==nums[left-1] and left<right : #这个要补上！！
                        left+=1
                    while nums[right]==nums[right+1] and left<right:
                        right-1
        return res
                

        