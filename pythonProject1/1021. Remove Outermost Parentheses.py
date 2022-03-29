class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        """
        解题思路：
        建立一个stack，count指针=0， 把第一个括号起始设置起始1，如果之后第一个左括号进stack，count+1（为2）， 右括号进stack，括号关闭，count回到1，
        """
        stack = []
        c = 0
        for i in s:
            if i == "(" and c == 0:  # 第一个左括号，进来counter变成1
                c = c + 1
            elif i == "(" and c != 0:  # 说明不是第一个括号，加入到stack，count加到2
                stack.append(i)
                c = c + 1
            elif i == ")" and c != 1:  # 如果count不是1，说明不是初始的左括号，此时加入到stack，counter从2减到1
                stack.append(i)
                c = c - 1
            else:  # i==")",c==1# count==1时， 说明是初始左括号，此时的右括号与左括号对应，count回到0
                c = c - 1
        return "".join(stack)