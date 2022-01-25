# 문제 설명 : words가 sorting 되어있는 배열일때, words에 있는 모든 문자들을 sorting 하여 리턴할 것.

# 연속한 값끼리만 비교하면됨. 건너뛰어서 체크할 필요는 없다. (연속되는 부분에서 메꿔짐)
# 두 값끼리의 순서리스트가 있을때 결과를 어떻게 구할지?
# topological sort. indegree가 0인 node부터 시작해서 출력. indegree인 노드가 여러개이면 error.

# REMIND : topological sort를 잘 쓴 문제.

class Solution:
    
    def alienOrder(self, words: List[str]) -> str:
        q, adj, indegree = deque(), defaultdict(list), defaultdict(int)
        
        for s in words:
            for c in s:
                indegree[c] = 0
        
        for i in range(len(words)-1):
            s1, s2 = words[i], words[i+1]
            l = min(len(s1), len(s2))
            for j in range(l):
                if s1[j] != s2[j]: 
                    adj[s1[j]].append(s2[j])
                    indegree[s2[j]] += 1
                    break
                if j == l-1 and len(s1) > len(s2):
                    return ""
        for c, v in indegree.items():
            if v == 0:
                q.append(c)
        ans = []
        print(q, adj)
        while q:
            c1 = q.popleft()
            ans.append(c1)
            for c2 in adj[c1]:
                indegree[c2] -= 1
                if indegree[c2] == 0:
                    q.append(c2)
        # cycle이 있으면 오류.
        print(ans, indegree)
        return "".join(ans) if len(ans) == len(indegree.keys()) else ""