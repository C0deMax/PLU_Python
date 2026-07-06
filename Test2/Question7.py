class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) > 0:
            print(self.stack[-1])


s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.push(20)

s.peek()