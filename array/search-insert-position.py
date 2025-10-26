class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 
        
        def search(left,right):
            if left> right:
                return left
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
                return search(left,right)
            elif nums[mid]<target:
                left=mid+1
                return search(left,right) #每一次都要向上return
            else:
                return mid
        return search(0,len(nums)-1)