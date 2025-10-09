class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # for i in range(len(nums)): 
        #一旦 pop(i) 删除当前元素，后面的元素会整体左移，接着 i 还会自增，结果就跳过了紧挨着的那个元素。所以不行
        #     if nums[i]==0: 
        #         nums.pop(i)
        #         nums.append(0)
        #（两指针，原地，稳定顺序，O(n)）
        index=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index]=nums[i]
                index+=1
        for i in range(index,len(nums)):
                nums[i]=0