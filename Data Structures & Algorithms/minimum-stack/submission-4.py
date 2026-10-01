class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minimum = val
        else:
            self.stack.append(val - self.minimum)
            self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        pop = self.stack.pop()

        if pop < 0:
            self.minimum -= pop


    def top(self) -> int:
        top = self.stack[-1]

        if top > 0:
            return self.minimum + top
        else:
            return self.minimum

    def getMin(self) -> int:
        return self.minimum
