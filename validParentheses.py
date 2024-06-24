class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        openBrackets = set(closeToOpen.values())

        for c in s:
            if c in openBrackets:  # If c is an opening bracket
                stack.append(c)
            elif c in closeToOpen:  # If c is a closing bracket
                if not stack or stack[-1] != closeToOpen[c]:
                    return False
                stack.pop()
            else:
                return False  # If c is not a valid bracket, return False immediately

        return not stack  # Return True if stack is empty

solution = Solution()
print(solution.isValid('()'))
