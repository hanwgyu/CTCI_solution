# Solution : 그래프가 Directed Acyclic Graph(DAG)이면 수강가능. Topological sort 알고리즘.

# Solution 1 : Topological sort by Indegree . Time : O(|V|+|E|), Space : O(N)

from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ready, adj_list, indegree = deque(), defaultdict(list), defaultdict(int)
        output = 0
        for e in prerequisites:
            adj_list[e[1]].append(e[0])
            indegree[e[0]] += 1
        for i in range(numCourses):
            if i not in indegree:
                ready.append(i)
        while len(ready) > 0:
            node = ready.popleft()
            output += 1
            for n in adj_list[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    ready.append(n)     
        if output == numCourses:
            return True
        return False
