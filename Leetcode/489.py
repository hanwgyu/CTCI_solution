# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        rotate = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
        room, r, c, = robot.room, robot.row, robot.col
        M, N = len(room), len(room[0])
        
        def dfs(r, c, rot):
            robot.clean()
            room[r][c] = -1
            for _ in range(4):
                r_, c_ = r+rotate[rot][0], c+rotate[rot][1]
                if 0 <= r_ < M and 0 <= c_ < N and room[r_][c_] == 1:
                    robot.move()
                    dfs(r_, c_, rot)
                rot = (rot+1)%4
                robot.turnRight()
            # go back
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        dfs(r,c, 0)
