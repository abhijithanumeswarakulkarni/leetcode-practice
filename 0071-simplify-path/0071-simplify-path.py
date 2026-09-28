class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        n = len(path)
        index = 0

        while index < n:
            char = path[index]
            if char == '/' :
                if (not stack or stack[-1] != char):
                    stack.append(char)
                index += 1
            # elif char == '.':
            #     temp = ""
            #     while char == '.':
            #         temp += char
            #         index += 1
            #         if index >= n:
            #             break
            #         char = path[index]
            #     if temp == '.' and (char == '/' or index == n):
            #         continue
            #     elif temp == '..' and (char == '/' or index == n):
            #         if len(stack) >= 2:
            #             stack.pop()
            #             stack.pop()
            #     else:
            #         stack.append(temp)
            else:
                temp = ""
                while char != '/':
                    temp += char
                    index += 1
                    if index >= n:
                        break
                    char = path[index]
                if temp == '.' and (char == '/' or index == n):
                    continue
                elif temp == '..' and (char == '/' or index == n):
                    if len(stack) >= 2:
                        stack.pop()
                        stack.pop()
                else:
                    stack.append(temp)
            # else:
            #     index += 1

        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        
        return "".join(stack)