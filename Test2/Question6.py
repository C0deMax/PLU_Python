class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()

    def display(self):
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i])


s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.push(20)

s.pop()

s.display()