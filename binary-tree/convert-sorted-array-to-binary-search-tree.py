# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #也是用dfs 然后要建立node node的左右都要
        def get_node(left,right):
            if left>right:
                return 
            mid=(left+right)//2
            root= TreeNode(nums[mid])#操作
            #很难想 node就是中间值了
            root.left=get_node(left,mid-1) #也是一个node ,就是下个的中间值：左边
            root.right=get_node(mid+1,right)   #也是一个node ,就是下个的中间值：右边 
            return root
        
        return get_node(0, len(nums)-1)

        