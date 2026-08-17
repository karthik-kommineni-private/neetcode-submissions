class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = path.split("/")

        stack = []

        for x in new_path:
            if x == "..":
                if stack:
                 stack.pop()
            elif x == "" or x == ".":
                continue
            else:
                stack.append(x)

        return "/" + "/".join(stack)            
      
        