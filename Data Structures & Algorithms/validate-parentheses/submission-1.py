class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parens = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in parens:
                stack.append(parens[c])
            elif len(stack) == 0 or stack.pop() != c:
                return False

        return not len(stack)
