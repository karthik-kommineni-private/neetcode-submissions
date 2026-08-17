class Solution:
    def isValid(self, s: str) -> bool:
        s_map = {')':'(','}':'{', ']':'['}
        stack = []

        for c in s:
            if c not in s_map.keys():
                stack.append(c)
                continue
            if not stack and s_map.get(c) != stack[-1]:
                return False

        return True        


        