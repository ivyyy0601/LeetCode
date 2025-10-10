class Solution(object):
    def search(self, nums, target):
        if nums is None or len(nums)==0:
            return -1
        l=0
        r=len(nums)-1
        mid=r+l/2
        while r>l:
            mid=r+l/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l= mid+1
        return -1
