# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append(root) # add root initially if not empty
        depth = 0

        while queue:
            depth += 1
            # go layer by layer
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            

        return depth
        
    

'''
BFS -> layer by layer --> Queue

[2,3,4]
'''