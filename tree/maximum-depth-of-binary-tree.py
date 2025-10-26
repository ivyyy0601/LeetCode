# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # #1. 递归 前中后 容易理解 dfs
        # def depth(root):
        #     if not root:
        #         return 0
        #     left= depth(root.left)
        #     right= depth(root.right)
        #     return max(left,right)+1

        # return depth(root)
        #简易的dfs
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        #用bfs也可以 就是要queue
        if not root:
            return 0
        #初始化
        max_depth=0 #一个节点就是1了
        queue=deque()
        queue.append(root)

        while queue:
            nums=len(queue)
            for i in range(nums):
                element= queue.popleft()
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
                    #nums=len(queue) #该层有的节点
            max_depth+=1 #结束该层 就depth+1
        return max_depth

        