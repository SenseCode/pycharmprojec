class Solution:
    def parseTernary(self, expression: str) -> str:
        '''
        Input: expression = "T?2:3"
        Output: "2"
'''

        i = len(expression) - 1
        stack = []
        while i >= 0:
            ch = expression[i]
            if ch.isdigit():
                stack.append(ch)
                i = i - 1
            elif ch in ("T", "F"):
                stack.append(ch)
                i = i - 1
            elif ch == ":":
                i = i - 1
            elif ch == "?":
                i = i - 1
                true = stack.pop()
                false = stack.pop()
                if expression[i] == "T":
                    stack.append(true)
                else:
                    stack.append(false)

                i = i - 1
        return stack[-1]
