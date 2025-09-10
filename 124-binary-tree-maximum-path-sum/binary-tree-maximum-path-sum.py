# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum=root.val

        def dfs(root):
            if not root:
                return 0
            nonlocal max_sum
            
            left_gain=max(0,dfs(root.left))
            right_gain=max(0,dfs(root.right))

            curr=root.val+left_gain+right_gain
            max_sum=max(max_sum,curr)

            return root.val+max(left_gain,right_gain)
        dfs(root)

        return max_sum


        # q=deque()
        # q.append(root)
        # max_sum=float('-inf')
        # curr=0

        # while q:
        #     node=q.popleft()
        #     curr=node.val+ node.left +node.right
        #     q.append(node.left)
        #     q.append(node.right)
        #     max_sum=max(curr,max_sum)
        # return max_sum


        