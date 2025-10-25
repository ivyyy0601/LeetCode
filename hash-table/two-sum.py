class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #因为他不是sorted的 而且要返回原来index的数值
        hashtable={}
        for i in range(len(nums)):
            if target-nums[i] in hashtable:
                return [i,hashtable[target-nums[i]]]
            hashtable[nums[i]] = i
