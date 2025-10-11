class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # #扩展法：后面的值加到前面去
        # result=[]
        # result.append([])
        # for num in nums:
        #     temp=[]
        #     for res in result:
        #         r=res[:]
        #         r.append(num)
        #         temp.append(r)
        #     for t in temp:
        #         result.append(t)
        # return result
        #用backtracking
        result, path = [], []          # result 存答案；path 是当前构建中的子集
        def backtracking(index: int) -> None:
            result.append(path[:])     # 走到任意节点，当前 path 就是一个子集（要拷贝）
            for i in range(index, len(nums)):   # 只能向后选，避免重复/倒退
                path.append(nums[i])            # 选择 nums[i]
                backtracking(i + 1)             # 继续从下一位开始做选择
                path.pop()                      # 撤销选择（回溯）

        backtracking(0)               # 从下标 0 开始
        return result