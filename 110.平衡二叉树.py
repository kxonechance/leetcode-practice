#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            height_l, flag_l = dfs(root.left)
            height_r, flag_r = dfs(root.right)
            if flag_l is False or flag_r is False or abs(height_l - height_r) > 1:
                return -1, False
            return max(height_l, height_r) + 1, True

        _, res = dfs(root)

        return res
# @lc code=end

