class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #法1️⃣hashtable
        # count={}
        # num=len(nums)
        # for n in nums:
        #     count[n] = count.get(n, 0) + 1
        # for k,v in count.items():
        #     if v > num/2:
        #         return k
        # return 0
        #法2️⃣： 如果一个数出现次数超过一半（> n/2）
        # nums.sort()
        # return nums[len(nums)//2]
        #法3️⃣ divide & conquer

        def getmaj(left,right) -> int:
            if left==right:
                return nums[left]
            mid=(left+right)//2
            left_mar = getmaj(left, mid)
            right_mar= getmaj(mid+1,right)
            if left_mar==right_mar:
                return left_mar
            left_count=0
            right_count=0
            for i in nums:
                if i==left_mar:
                    left_count+=1
                elif i == right_mar:
                    right_count+=1
            if left_count>=right_count:
                return left_mar
        return getmaj(0,len(nums)-1)
