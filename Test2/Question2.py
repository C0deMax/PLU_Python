class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        values = [10, 20, 30, 40, 50]

        self.head = Node(values[0])
        current = self.head

        for value in values[1:]:
            current.next = Node(value)
            current = current.next

    def insert_after_20(self):
        current = self.head

        while current:
            if current.data == 20:
                new_node = Node(25)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next


ll = LinkedList()
ll.create()
ll.insert_after_20()
ll.display()