class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for x in s:
            if stack == [] and x in d:
                return False
            elif stack == [] or x not in d:
                stack.append(x)
            elif x in d and stack[-1] == d[x]:
                stack.pop()
            else: return False
        return stack == []