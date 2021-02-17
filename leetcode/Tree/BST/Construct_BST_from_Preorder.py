# Leetcode 1008. Construct Binary Search Tree from Preorder Traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i<len(preorder) and preorder[i] < root.val:
            i+=1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

        # Below Solution using left and right variables
        # instead of using the slice function

        """
        if not preorder:
            return None
        
        return self.construct(preorder, 0, len(preorder))
    
    def construct(self, preorder, l, r):
        if l >= r:
            return None
        
        root = TreeNode(preorder[l])
        i = l+1
        
        while(i < r and preorder[i] < root.val):
            i += 1
    
        root.left = self.construct(preorder, l+1, i)
        root.right = self.construct(preorder, i, i + (r-i))
        
        return root
        """


Run = Solution()
Run.bstFromPreorder([8,5,1,7,10,12])
