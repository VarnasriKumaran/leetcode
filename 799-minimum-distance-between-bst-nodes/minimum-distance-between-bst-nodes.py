# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_diff=float('inf')
        res=self.inorder(root)
        for i in range(1,len(res)):
            min_diff=min(min_diff,res[i]-res[i-1])
        return min_diff


    def inorder(self,root):
        if not root:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)


        