class TreeNode:
    def __init__(self,val):
        self._left = None
        self._right = None
        self._val = val
        
    def bst_insert(self,root,node):
        if root is None:
            return node
        elif root._val > node._val:
            root._left = self.bst_insert(root._left,node)
        elif root._val < node._val:
            root._right = self.bst_insert(root._right,node)
        return root
