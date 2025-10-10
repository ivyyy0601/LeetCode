class Solution(object):
    def search(self, nums, target):
        if nums is None or len(nums)==0:
            return -1
        l=0
        r=len(nums)-1
        while r>=l:  #要注意这个 如果只有一个的时候 为0的时候
            mid = (r + l) // 2 #索引必须是整数
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l= mid+1
        return -1
