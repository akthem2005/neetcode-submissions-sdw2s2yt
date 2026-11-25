class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(":")", "{":"}", "[":"]"}
        for x in s:
            if not stack:
                if x not in d:
                    return False
                stack.append(x)
            else:
                if x in d:
                    stack.append(x)
                else:
                    if d[stack[-1]] == x:
                        stack.pop()
                    else:
                        return False
        return True if not stack else False
