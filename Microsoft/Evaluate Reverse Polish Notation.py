#problem link
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        for i in range(n):
            if tokens[i] in ['+','-','*','/']:
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == '+':
                    z = a+b
                    stack.append(z)
                elif tokens[i] == '*':
                    z = a*b
                    stack.append(z)
                elif tokens[i] == '-':
                    z = b-a
                    stack.append(z)
                else:
                    z = b/a
                    stack.append(z)
                continue
            stack.append(tokens[i])
        return int(stack[0])
