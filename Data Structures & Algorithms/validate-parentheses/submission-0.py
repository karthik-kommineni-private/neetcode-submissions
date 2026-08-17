class Solution:
    def isValid(self, s: str) -> bool:
        
        s_map = {')': '(', '}':'{', ']':'['}
        stack = []
        for i in range (len(s)):
            if s[i] in s_map:
               if s_map[s[i]] != stack[-1]:
                    return False
               else:
                stack.pop()
            else:     
                stack.append(s[i])

        return True    
        