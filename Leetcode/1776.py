# 문제 설명 : 차들이 같은 방향으로 다른 속도로 움직임. 충돌하면 하나로 합쳐져서 느린 차의 속도로 움직임
# 충돌하게 되는 시간을 구하라.

# 오른쪽에서 시작해서 이웃된 노드를 기준으로 구해나가면됨.
# 현재 차의 속도는 이전차와는 무관함. 자기가 부딪히는 차와만 관련이 있음.
# 다음차가 그 다음차와 먼저 부딪혀버리면 시간 계산이 그 다음차를 기준으로 되어야함.
# 충돌 시간이 작아지는 순서대로 index에 대한 스택을 쌓음. 뒷부분 차들의 더 짧은 충돌시간은 고려할 필요 없음. 
# 충돌 시간을 고려할때 각 뒷차에서의 충돌시간을 고려하고 점점 커지는 순서대로 비교해 pop. 마지막 index 와의 충돌시간을 저장하면 된다.

# REMIND: Trapping rain water과 비슷한 stack 사용하는 문제. 그러나 훨씬 어렵고 중요하다.

class Solution:
    def getCollisionTimes(self, A: List[List[int]]) -> List[float]:
        N = len(A)
        st = [N-1] # index
        res = [-1] * N
        for i in reversed(range(N-1)):
            p, s = A[i]
            # 스피드가 더 느리거나 시간이 더 오래걸릴때 pop함 
            while st and (s <= A[st[-1]][1] or (A[st[-1]][0]-p)/(s - A[st[-1]][1]) >= res[st[-1]] >= 0):
                st.pop()
            if st:
                res[i] = (A[st[-1]][0]-p)/(s - A[st[-1]][1])
            st.append(i)
        return res