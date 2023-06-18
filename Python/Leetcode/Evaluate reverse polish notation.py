class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+", "-", "*", "/"]

        for t in tokens:
            if t in op:
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(x + y if t == '+' else y - x if t == '-' else x * y if t == '*' else int(y / x))
            else:
                stack.append(t)
        
        return int(stack[-1])