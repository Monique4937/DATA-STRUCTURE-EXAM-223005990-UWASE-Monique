class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.key, end=" ")


print("Binary Tree Implementation in Wedding Vendor Marketplace:")
bt = BinaryTree()

tasks = [
    "Assign Vendor A", 
    "Confirm Booking B", 
    "Send Invoice C", 
    "Resolve Inquiry D", 
    "Schedule Meeting E"
]


task_keys = [ord(task.split()[-1][0]) for task in tasks]


root = None
for key in task_keys:
    root = bt.insert(root, key)


print("\nInorder Traversal (Sorted Tasks):")
bt.inorder_traversal(root)

print("\n\nPreorder Traversal (Process Tasks):")
bt.preorder_traversal(root)

print("\n\nPostorder Traversal (Finalize Tasks):")
bt.postorder_traversal(root)
