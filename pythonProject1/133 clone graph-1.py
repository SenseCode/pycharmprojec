import collections
'''
解题思路：
建立一个dfs helper,建立一个old 图和新图对应的字典。
对于old里面的node，先查找在字典里么？在里面就return oldToNew[node],接着赋值给copy，不再里面就直接赋值给copy，copy的值应该是Node类型，val应该等于old图node的val
对于old图里面每一个neighbor进行dfs遍历，并把他们加入到新图copy的neighbors中，然后返回copy，new的copy图就建好了

最后调用helper，起始值为node,并对node进行判断。
'''

def cloneGraph(node):
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
    from collections import deque
    if not node:
        return node
    visited = {}
    queue = collections.deque([node])
    visited[node] = Node(node.val, [])

    while queue:
        n = queue.popleft()
        for nei in n.neighbors:
            if nei not in visited:
                visited[nei] = Node(nei.val, [])
                queue.append(nei)
            visited[n].neighbors.append(visited[nei])
    return visited[node]


adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
n = cloneGraph(adjList)
print(n)