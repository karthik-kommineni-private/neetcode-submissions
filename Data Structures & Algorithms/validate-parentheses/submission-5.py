class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or s == None:
            return False

        b_map = {')': '(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in b_map:
                if len(stack) == None and b_map[c] != stack.pop():
                    return False 
            else:
                #add to stack
                stack.append(c)

        return True



