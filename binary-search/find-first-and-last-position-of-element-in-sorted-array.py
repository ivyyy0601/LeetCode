class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left= 0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target: #因为我们要找>=
                left=mid+1
            else:
                right=mid-1
        if right == len(nums) or nums[right] != target:
            return [-1, -1]
        left2= 0
        right2=len(nums)-1
        while left2<=right2:
            mid2=(left2+right2)//2
            if nums[mid2]<target+1: #因为我们要找>=
                left2=mid+1
            else:
                right2=mid-1
        return [right,right2-1]
        
        
        