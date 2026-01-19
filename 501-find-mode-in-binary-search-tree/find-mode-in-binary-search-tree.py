# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr=self.inorder(root)
        n=Counter(arr)
        max_freq=max(n.values())
        res=[]
        for i,j in n.items():
            if j==max_freq:
                res.append(i)
        return res
    def inorder(self,root):
        if not root:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)