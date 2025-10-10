class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums)==0:
            return 0
        l=0
        r=len(nums)-1
        while r>=l:
            mid = l+r//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return l