from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        # use dfs or bfs all fine, here use dfs.
        # record all visited room in visited.
        # compared visited length 是否等于rooms的length，来最终确定是不是visit了所有的房间。

        visited = set()

        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)

        return len(visited) == len(rooms)

    # # BFS:
    #     visited = {0} #visited = set()
    #     queue = deque()
    #     queue.append(0)
    #
    #     while queue:
    #         room = queue.popleft()
    #
    #         for key in rooms[room]:
    #             if key not in visited:
    #                 visited.add(key)
    #                 queue.append(key)
    #     return len(visited) == len(rooms)