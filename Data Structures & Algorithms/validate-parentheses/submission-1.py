class Solution:
    def isValid(self, s: str) -> bool:
        
        s_map = {')': '(', '}':'{', ']':'['}
        stack = []
        for i in range (len(s)):
            if s[i] in s_map:
                if not stack or stack[-1] != s_map[s[i]]:
                    return False
                stack.pop()  # Pop the matched opening bracket
            else:     
                stack.append(s[i])

        return not stack    
        