# bfs + visited

class Solution:
    def minKnightMoves(self, t_x: int, t_y: int) -> int:
        visited = set([(0,0,0)])
        q = deque([(0,0,0)]) #x,y,n
        
        while q:
            x,y,n = q.popleft()
            if x == t_x and y == t_y:
                return n
            for diff in [(2,1),(1,2),(-1,2),(-2,1),(-1,-2),(-2,-1),(1,-2),(2,-1)]:
                x_,y_ = x+diff[0], y+diff[1]
                if (x_,y_) not in visited and -302<= x_ <=302 and -302<= y_ <=302:                    
                    q.append((x_,y_,n+1))
                    visited.add((x_,y_))
        return -1