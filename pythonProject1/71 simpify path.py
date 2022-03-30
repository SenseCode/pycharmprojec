class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        print(path.split("/"))
        for portion in path.split("/"):  # "/home/.."，--> ['', 'home', '..']

            if portion == "..":
                if stack:
                    stack.pop()  # 把最后一级pop出来，返回上一级
            elif portion == "." or not portion:  # 是,,就是本级目录，不做任何操作。

                continue
            else:
                stack.append(portion)
        final_str = "/" + "/".join(stack)
        return final_str