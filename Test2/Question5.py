class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def display(self):
        print("Stack Elements:")

        for item in self.items:
            print(item)


stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)

stack.display()