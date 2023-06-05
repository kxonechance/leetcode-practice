#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, target):
            if not root:
                return False
            if root.left is None and root.right is None:
                if target == root.val:
                    return True
                else:
                    return False
            return dfs(root.left, target - root.val) or dfs(root.right, target - root.val)

        return dfs(root, targetSum)
 
# @lc code=end

