class Solution(object):
    def removeElement(self, nums, val):
        slow=0
        fast=0
        for fast in range(len(nums)):
            if nums[fast]!= val:
                nums[slow]=nums[fast]
                slow+=1
        return slow