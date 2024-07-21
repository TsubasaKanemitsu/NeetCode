from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithmetic_operations = {"+", "-", "*", "/"}
        for token in tokens:
            if token in arithmetic_operations:
                b, a = stack.pop(), stack.pop()
                # print(b, a)
                stack.append(self.calculation(int(a), int(b), token))
            else:
                stack.append(token)
        return stack[-1]

    def calculation(self, a, b, operation):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return int(a / b)
        
s = Solution()
print(s.evalRPN(tokens=["4","6","9","3","+","-11","*","/","*","17","+","5","+"]))