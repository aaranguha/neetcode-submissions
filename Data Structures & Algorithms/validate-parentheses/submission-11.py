class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c not in closed:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if popped != closed[c]:
                    return False
        if len(stack) == 0:
            return True
        return False
                