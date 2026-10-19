class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c not in closed:
                stack.append(c)
            if c in closed:
                if not stack:
                    return False
                popped = stack.pop()
                if closed[c] != popped:
                    return False
        return not stack
                