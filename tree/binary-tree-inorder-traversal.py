# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # #递归的形式
        # def dfs(node):
        #     if node is None:
        #         return
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)
        # res=[]
        # dfs(root)
        # return res
        #非递归： 一路向left 放到stack 里面，然后到底之后pop出stack的东西 存到result里面 然后往右边看
        res=[] #存的是数值
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left

            element=stack.pop()
            res.append(element.val)
            root=element.right

        return res
        

        