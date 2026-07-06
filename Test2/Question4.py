class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        self.head = Node(10)
        self.head.next = Node(20)
        self.head.next.next = Node(30)
        self.head.next.next.next = Node(40)
        self.head.next.next.next.next = Node(50)

    def countNodes(self):
        temp = self.head
        count = 0

        while temp != None:
            count += 1
            temp = temp.next

        print("Total nodes:", count)


l = LinkedList()
l.create()
l.countNodes()