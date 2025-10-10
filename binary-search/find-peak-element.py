class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(n - 1):
        #     if nums[i] > nums[i + 1]:
        #         return i  # 第一个下降点前一个就是峰值
        # return n - 1  # 如果一直递增，最后一个是峰值  这个是O（n）的方法
        if nums is None or len(nums)==0:
            return -1
        l=0
        r=len(nums)-1
        while r>l: # ← 保证 mid+1 不越界
            mid= (r+l)//2 
            if nums[mid]<nums[mid+1]: #我比右边小  单调增加，往右边 右边有可能有大的
                l=mid+1
            else:
                r=mid #我比右边大， 所以左边有可能有大的
        return l #最后肯定是l和r相遇了，就是最大的数
            