class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        解题思路：
        这道题要读懂，根据举例可以看出，每一步返回的结果要重新再计算各个digit的square的和，必须写一个function进行功能调用。
        如果每一步的结果在一个set里面存在，则说明是个circle，无法得出结果，请想象成一个图。
        写一个base的function来计算digit square和
        然后根据circle的查找方法，建立一个set，查看每一个值n是否在set里面，直到n的结果是1，或者不是1的时候，but in seen
        '''

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum = total_sum + digit ** 2  ##must be **2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:  # must be while loop
            seen.add(n)
            n = get_next(n)
        return n == 1
