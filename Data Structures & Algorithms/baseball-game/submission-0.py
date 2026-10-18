class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for ops in operations:
            if ops == "C":
                stack.pop()
            elif ops == "D":
                stack.append(int(stack[-1])*2)
            elif ops == "+":
                stack.append(int(stack[-1])+int(stack[-2]))
            else:
                stack.append(int(ops))
        return sum(stack)