class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}

        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)
            else:
                if not stack:
                    return False

                if top := stack.pop():
                    if top != closeToOpen[bracket]:
                        return False

        if stack:
            return False
        
        return True