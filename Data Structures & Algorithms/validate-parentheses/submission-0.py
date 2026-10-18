class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for ch in s:
            if ch == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()

            elif ch == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()

            elif ch == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()

            else:
                stack.append(ch)

        return len(stack) == 0
