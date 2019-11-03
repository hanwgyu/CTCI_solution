# Solution : Stack 사용해 현재 처리중인 iter의 parent 노드들을 저장하면서 nextNode를 찾음.
# Time : avg O(1) (next, hasNext function), Space : O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = [] #node와 해당 node의 처리 상태 저장
        self.iter = self.findSmallestFromNode(root)
        
    def findSmallestFromNode(self, node: TreeNode):
        if not node:
            return None
        while node:
            self.stack.append([node, False])
            node = node.left
        return self.stack[-1][0]
    
    def next(self) -> int:
        if not self.iter:
            return None
        
        ans = self.iter.val
        self.stack[-1][1] = True 
        # find next iter
        if self.iter.right:
            self.iter = self.findSmallestFromNode(self.iter.right)
        else:
            while self.stack and self.stack[-1][1]:
                self.stack.pop()
            if self.stack:
                self.iter = self.stack[-1][0]
            else:
                self.iter = None
        return ans
        
            
    def hasNext(self) -> bool:
        return True if self.iter else False
