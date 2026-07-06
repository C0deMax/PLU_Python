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

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)


tree = BinaryTree()
tree.create()

print("Inorder Traversal:")
tree.inorder(tree.root)