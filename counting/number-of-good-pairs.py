class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             result+=1
        # return result
        # 这种偏慢 O(n²)

# range(1,2)包括1 不包可2
        d = {}                       # 用字典 d 记录每个数出现的次数。哈希表！！！
        for i in nums:               # 遍历数组
            if i in d:               # 如果 i 已经在字典里
                d[i] += 1            # 出现次数 +1
            else:
                d[i] = 1             # 否则初始化为 1

        count = 0
        for i in d:                  # 遍历每个不同的数
            n = d[i]                 # 取该数的出现次数
            x = n * (n-1) // 2       # 组合数公式 C(n,2) → 能组成的好对数量 记住！！！！！
            count += x               # 累加到结果里

        return count
        # x = n * (n-1) // 2 组合数公式 C(n,2) → 能组成的好对数量

