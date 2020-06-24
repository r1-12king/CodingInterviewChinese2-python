class StackWithMin:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, data):
        self.stack.append(data)

        if not self.minstack:
            self.minstack.append(data)
        else:
            # 如果当前元素比栈顶元素小，辅助栈压入当前元素，否则，继续压入栈顶元素
            if data < self.minstack[-1]:
                self.minstack.append(data)
            self.minstack.append(self.minstack[-1])

    def pop(self):
        if not self.stack or not self.minstack:
            return None
        self.minstack.pop()
        return self.stack.pop()

    def min(self):
        if not self.minstack:
            return None

        return self.minstack[-1]


if __name__ == "__main__":
    s = StackWithMin()
    s.push(2.98)
    s.push(3)
    print(s.stack)
    print(s.min())
    s.pop()
    print(s.stack)
    print(s.min())
    s.push(1)
    print(s.stack)
    print(s.min())
    s.pop()
    print(s.stack)
    print(s.min())
