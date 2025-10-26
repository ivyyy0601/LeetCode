# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter=0 
        #全局变量，小函数和大函数里面共用
        #其实就是左右节点的高度和的最大值
        def dfs_height(root):
            nonlocal max_diameter #让内层 dfs_height 能更新外层的 max_diameter。
            if not root:
                return 0
            left=dfs_height(root.left)
            right=dfs_height(root.right)
            max_diameter=max(left+right, max_diameter )#这个事全局变量
            return max(left,right)+1 #这个事计算高度的 不会变的
        
        dfs_height(root)
        return max_diameter

        