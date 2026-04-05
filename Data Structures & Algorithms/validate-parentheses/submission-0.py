class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        open_s = ['(', '{', '[']
        d = {'(':')', '{': '}', '[': ']'}
        for x in s:
            if x in d:
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                if x!=d[stack[-1]]:
                    return False
                else:
                    stack.pop()
        return stack == []
                
