def insert(intervals, newInterval):
    '''
    解题思路：
    存在三种情况：
    newinterval 在所有interval之前，或者之后， 或者和其中的一条有overlap
    那么对于在之前：直接append newInterval，返回newInterval+interals后面所有的
    对于newInterval start在任意i end 之后的，append intervals[i]
    '''
    res = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    res.append(newInterval)

    return res

intervals = [[1,3],[6,9]]
newInterval = [2,5]
s=insert(intervals,newInterval)
print(s)
