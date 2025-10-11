class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        n=len(nums)
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for k,v in count.items():
            if v > n/2:
                return k
        return 0
        