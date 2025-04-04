class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct(n):
    if n < 0:
        return None
    root = TreeNode(1)
    
    def build(node, height):
        if height == 0:
            return
        node.left = TreeNode(1)
        node.right = TreeNode(1)
        build(node.left, height - 1)
        build(node.right, height - 1)
    
    build(root, n - 1)
    return root