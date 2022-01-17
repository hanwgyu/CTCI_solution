# 오른쪽으로 가면 -1, 왼쪽으로 내려가면 +1.
# deque로 저장한후 list로 변경. deque의 0의 위치를 저장함.

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        bfs = deque([(root, 0)])
        base = 0
        
        while bfs:
            node, idx = bfs.popleft()
            if not node:
                continue
            h, l = len(q)-base-1, -base
            if h < idx:
                q.append([])
            elif l > idx:
                q.appendleft([])
                base += 1
            q[idx+base].append(node.val)
            bfs.append((node.left, idx-1))
            bfs.append((node.right, idx+1))
        return list(q)