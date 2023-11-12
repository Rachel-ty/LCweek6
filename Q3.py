class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rem=[]
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            rem.append(node.val)
            inOrder(node.right)
        inOrder(root)
        return rem[k-1]