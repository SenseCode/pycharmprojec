def canFinish(self, numCourses, prerequisites):


    preMap = {i: [] for i in range(numCourses)}

    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visitedSet = set()


    def dfs(crs):  # 开始对course进行dfs search，对于送进来的course
        if crs in visitedSet:
            return False  # 说明是个环形，已经被访问过
        if preMap[crs] == []:  # 说明不需要prerequire class就能完成，返回True
            return True

        visitedSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        visitedSet.remove(crs)
        preMap[crs] = []
        return True


    for crs in range(numCourses):  # in case [1,2], [3,4]这种断开的情况，需要挨个循环
        if not dfs(crs):
            return False
    return True