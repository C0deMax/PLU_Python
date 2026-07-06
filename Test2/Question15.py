class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create(self):
        self.root = Node(50)
        self.root.left = Node(30)
        self.root.right = Node(70)
        self.root.left.left = Node(20)
        self.root.left.right = Node(40)
        self.root.right.left = Node(60)
        self.root.right.right = Node(80)

    def countNodes(self, node):
        if node is None:
            return 0

        left = self.countNodes(node.left)
        right = self.countNodes(node.right)

        return 1 + left + right


tree = BinaryTree()
tree.create()

total = tree.countNodes(tree.root)

print("Total Nodes:", total)