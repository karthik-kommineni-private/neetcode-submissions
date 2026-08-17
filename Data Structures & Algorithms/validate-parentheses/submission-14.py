class Solution:
    def isValid(self, s: str) -> bool:
        s_map = {')':'(','}':'{', ']':'['}
        stack = []

        for c in s:
            if c not in s_map:
                stack.append(c)
            else:
                if not stack or s_map[c] != stack[-1]:
                    return False
                stack.pop()    

        return not stack               