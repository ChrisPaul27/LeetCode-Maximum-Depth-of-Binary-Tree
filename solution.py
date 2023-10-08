# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        path = 1
        
        if root == None:
            return 0
        else:
            return max(path + self.maxDepth(root.left), path + self.maxDepth(root.right))      
