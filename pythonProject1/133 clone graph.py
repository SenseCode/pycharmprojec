from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node) :
    # DFS method
    # old_to_new={}

    # def dfs(node):
    #     if node in old_to_new:
    #         return old_to_new[node]
    #     copy=Node(node.val)
    #     old_to_new[node]=copy
    #     for nei in node.neighbors:
    #         copy.neighbors.append(dfs(nei))

    #     return copy
    # return dfs(node) if node else None

    # BFS method
    # import collections
        if not node:
            return node
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    queue.append(nei)
                visited[n].neighbors.append(visited[nei])
        return visited[node]

    adjList = [[2,4],[1,3],[2,4],[1,3]]
    n=cloneGraph(adjList)
    print(n)



