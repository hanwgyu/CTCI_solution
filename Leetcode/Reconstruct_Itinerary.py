# Solution : 한붓그리기. DFS를 통해 만약 더이상 갈곳이 없으면 값을 저장.

# adjacent list를 만들고, dfs로 알파벳 반대 순으로 방문하고, 방문할 노드가 없으면 추가한 후, 거꾸로 뒤집으면 답이 나온다.

# Time : O(E), Space : O(E+V)

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(src: str):
            print(d[src])
            while d[src]:
                dst = d[src].pop()
                dfs(dst)
            ans.append(src)

        d, ans = defaultdict(list), []
        for src, dst in sorted(tickets, reverse=True):
            d[src].append(dst)
        dfs("JFK")
        return ans[::-1]
