class Solution(object):#[left,right）
    def search(self, nums, target):
        left=0
        right=len(nums)
        while left<right:
            middle=(left+right)//2
            if (nums[middle]>target):
                right=middle
            elif (nums[middle]<target):
                left=middle+1
            else:
                return middle
        return -1
        