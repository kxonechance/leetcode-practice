#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 and root2:
                return False
            if root1 and not root2:
                return False
            if root1 and root2:
                if root1.val == root2.val:
                    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)
                else:
                    return False

        def dfs(root, sub_root):
            if not root and not sub_root:
                return True
            if not root or not sub_root:
                return False
            if is_same_tree(root, sub_root):
                return True
            else:
                return dfs(root.left, sub_root) or dfs(root.right, sub_root)

        return dfs(root, subRoot)
# @lc code=end

