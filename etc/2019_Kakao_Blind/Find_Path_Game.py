from collections import defaultdict, deque
import sys
class TreeNode:
    def __init__(self, idx):
        self.idx = idx
        self.l_min = float('-inf')
        self.r_max = float('inf')
        self.left = None
        self.right = None

def solution(nodeinfo):
    def traverse(node, a, post):
        if not node:
            return
        if not post:
            a.append(node.idx)
        traverse(node.left, a, post)
        traverse(node.right, a, post)
        if post:
            a.append(node.idx)
    sys.setrecursionlimit(10**6)
    #TreeNode를 생성해서 각 level에 대한 x 오름차순 sort된 array를 생성.이것들을 dict으로 관리.
    y_nodes = defaultdict(list)
    for i, (x, y) in enumerate(nodeinfo):
        y_nodes[y].append((x, TreeNode(i+1))) 
    for nodes in y_nodes.values():
        nodes.sort()
    ys = sorted(y_nodes.keys(),reverse=True)
    
    #위 level의 queue부터 순회하면서 다음 level의 queue와 two pointer로 움직이면서 연결
    y_i = 0
    for y_i in range(len(ys)-1):
        nodes, next_nodes = y_nodes[ys[y_i]], y_nodes[ys[y_i+1]]
        i, j = 0, 0
        while i < len(nodes) and j < len(next_nodes):
            x, node, next_x, next_node = nodes[i][0], nodes[i][1], next_nodes[j][0],  next_nodes[j][1]
            if node.l_min < next_x < x:
                node.left, next_node.l_min, next_node.r_max = next_node, node.l_min, x
                j += 1
            elif x < next_x < node.r_max:
                node.right, next_node.l_min, next_node.r_max = next_node, x, node.r_max
                j += 1
            else:
                i += 1
    root = y_nodes[ys[0]][0][1]
    pre, post = [], []
    traverse(root, pre, False)
    traverse(root, post, True)
    return [pre,post]
            
