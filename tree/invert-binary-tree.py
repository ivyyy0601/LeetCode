# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #dfs或者bfs都可以
        #dfs
        # def reverse(root):
        #     if not root:
        #         return
        #     root.left, root.right = root.right, root.left
        #     reverse(root.left)
        #     reverse(root.right)
        # reverse(root)
        # return root
        #bfs
        if not root:
            return 
        queue=deque([root])
        while queue:
            # ele_len=len(queue)
            # for _ in range(ele_len):#因为我们只需要管每个元素 不需要说管每一层怎么样
            element=queue.popleft()
            element.left, element.right = element.right, element.left #取出来的操作
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)
            
        return root
        