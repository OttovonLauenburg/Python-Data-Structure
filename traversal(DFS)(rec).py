# Tree Traversal
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
def inorder(root):
    rlist = []
    if root is not None:
        if root.left is not None:
            rlist.append(inorder(root.left))
        rlist.append(root.val)
        if root.right is not None:
            rlist.append(inorder(root.right))
    return rlist
    
def preorder(root):
    prelist = []
    if root is not None:
        prelist.append(root.val)
        if root.left is not None:
            prelist.append(preorder(root.left))
        if root.right is not None:
            prelist.append(preorder(root.right))
    return prelist
    
def postorder(root):
    postlist = []
    if root is not None:
        if root.left is not None:
            postlist.append(postorder(root.left))
        if root.right is not None:
            postlist.append(postorder(root.right))
        postlist.append(root.val)
    return postlist
