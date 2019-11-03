# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.iter = -1
        self.list = []
        self.getBSTList(root, self.list)
   
    def getBSTList(self, root: TreeNode, d: List[int]):
        if not root:
            return
        self.getBSTList(root.left, d)
        d.append(root.val)
        self.getBSTList(root.right, d)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.hasNext():
            return None
        self.iter += 1
        return self.list[self.iter]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.list) <= self.iter + 1:
            return False
        return True
