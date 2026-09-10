class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list(int) = []
        while len(tokens):
            token = tokens.pop(0)

            match token:
                case "+":
                    stack.append(stack.pop(-2) + stack.pop(-1))
                case "-":
                    stack.append(stack.pop(-2) - stack.pop(-1))
                case "*":
                    stack.append(stack.pop(-2) * stack.pop(-1))
                case "/":
                    stack.append(int(stack.pop(-2) / stack.pop(-1)))
                case _:
                    stack.append(int(token))

        return stack[0]
