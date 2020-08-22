# Solution : DFS. Set에 룸을 추가해가면서, DFS를 돈 후 모든 룸이 추가되었으면 True.
# Time : O(|V|+|E|), Space : O(|V|)


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room: int):
            if room in s:
                return
            s.add(room)
            for key in rooms[room]:
                dfs(key)

        s = set()
        dfs(0)
        return len(s) == len(rooms)
