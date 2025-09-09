#Definition for a binary tree node.
# class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return root.val==root.left.val+root.right.val

# 在 LeetCode 里，不需要手动声明 root 是 TreeNode，平台已经帮你做了；
# 但在本地跑的时候，如果你要自己调试，就要自己写 root = TreeNode(10, TreeNode(4), TreeNode(6))。
        