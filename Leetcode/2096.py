# Solution 1: dfs 순회하면서 위치를 2진수로 표현한후, 두 숫자를 비교해 계산.
# 앞에서부터 겹치는 숫자 외에는 U로 제거하고, LR로 추가함.
# ex) 100 110 , 100 -> 1 -> 110

# Solution 2: 두 value를 공통으로 child로 가지는 가장 아래쪽 node를 리턴. (lca)
# lca로부터 경로를 찾아서 리턴.

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(cur: TreeNode) -> TreeNode: # least common ancestor
            if not cur:
                return None
            if cur.val in (startValue, destValue):
                return cur
            left, right = lca(cur.left), lca(cur.right)
            return cur if left and right else left or right
        
        root = lca(root)
        
        st = [(root, "")]
        path1, path2 = None, None
        while st and (not path1 or not path2):
            node, path = st.pop()
            if node.val == startValue: path1 = path
            if node.val == destValue: path2 = path
            if node.left: st.append((node.left, path+"L"))
            if node.right: st.append((node.right, path+"R"))
        return "U" * len(path1) + path2
        
        
    
    def getDirections_1(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(cur: TreeNode, target: int, loc: str='1') -> str:
            if not cur:
                return ''
            if cur.val == target:
                return loc
            return dfs(cur.left, target, loc+'0') or dfs(cur.right, target, loc+'1')
            
        s1 = dfs(root, startValue)
        s2 = dfs(root, destValue)
        
        def up(i) -> str:
            return 'U' * (len(s1) - i)
        
        def down(i) -> str:
            move = ''
            while i < len(s2):
                move = move + 'L' if s2[i] == '0' else move + 'R'
                i += 1
            return move
        
        i = 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i += 1
        if i == len(s1):
            ans = down(i)
        elif i == len(s2):
            ans = up(i)
        else:
            ans = up(i) + down(i)
        return ans