#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0

        def dfs(root, target):
            if not root:
                return {}
            l = dfs(root.left, target)
            r = dfs(root.right, target)
            c = {root.val: 1}
            for k, v in l.items():
                c[root.val + k] = c.get(root.val + k, 0) + v
            for k, v in r.items():
                c[root.val + k] = c.get(root.val + k, 0) + v
            for k, v in c.items():
                if k == target:
                    self.res += v
            return c

        dfs(root, targetSum)

        return self.res
# @lc code=end

