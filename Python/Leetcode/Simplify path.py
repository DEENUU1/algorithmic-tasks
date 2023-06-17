class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        tokens = path.split("/")

        for token in tokens:
            if token == "..":
                if stack:  
                    stack.pop()  
            elif token and token != ".":
                stack.append(token)  

        return "/" + "/".join(stack)
        
