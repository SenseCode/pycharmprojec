class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        解题思路：
        two pointers和stack的方法时间复杂度都是一样的O（m+n）
        使用stack的方法好一点
        首先简历一个helper function， 对字符串里的每一个字母，如果不是#，就加入到ans array里，
        如果是#， 如果ans有值，就把最顶上的pop出来（stack后进后出）
        循环完所有字母都把ansstack内的字母连接起来Join，然后使用这个helper对S,T分别循环，判断两个值是否相等。

        '''

        def helper(s):
            ans = []
            for c in s:
                if c != '#'
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)

        return helper(s) == helper(t)
