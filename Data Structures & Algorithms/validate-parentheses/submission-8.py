class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or s == None:
            return False

        b_map = {')': '(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in b_map:
                if len(stack) == 0 or b_map[c] != stack.pop(): 
                    return False    
            else:
                #add to stack
                stack.append(c)

        if len(stack) > 0:
            return False        

        return True



