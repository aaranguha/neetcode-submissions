class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {')' : '(', ']' : '[', '}' : '{'}

        for c in s:
            if c not in p_map:
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != p_map[c]:
                    return False
        return not stack