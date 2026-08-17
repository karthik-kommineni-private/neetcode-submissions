class Solution:
    def isValid(self, s: str) -> bool:
        s_map = {')':'(','}':'{', ']':'['}
        stack = []

        for c in s:
            if c not in s_map.keys():
                stack.append(c)
                continue
            if not stack or s_map.get(c) != stack.pop():
                return False

        return not stack        


        