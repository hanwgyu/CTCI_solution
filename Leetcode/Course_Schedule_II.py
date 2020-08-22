# Solution : 그래프가 Directed Acyclic Graph(DAG)이면 수강가능. Topological sort 알고리즘.

# Solution 1 : Topological sort by Indegree . Time : O(|V|+|E|), Space : O(|V|+|E|)

from collections import defaultdict, deque


class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        ready, adj_list, indegree = (
            deque(),
            defaultdict(list),
            defaultdict(int),
        )
        output = []
        for e in prerequisites:
            adj_list[e[1]].append(e[0])
            indegree[e[0]] += 1
        for i in range(numCourses):
            if i not in indegree:
                ready.append(i)
        while len(ready) > 0:
            node = ready.popleft()
            output.append(node)
            for n in adj_list[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    ready.append(n)
        if len(output) != numCourses:
            return []
        return output
