class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display_tree(self, level=0):
        print(" " * level * 4 + "|-- " + self.data)  
        for child in self.children:
            child.display_tree(level + 1)


def build_vendor_tree():
    root = TreeNode("Wedding Vendor Marketplace")

    
    catering = TreeNode("Catering Services")
    decoration = TreeNode("Decoration Services")
    photography = TreeNode("Photography & Videography")

    
    catering.add_child(TreeNode("Buffet Catering"))
    catering.add_child(TreeNode("Plated Catering"))
    catering.add_child(TreeNode("Food Trucks"))

    
    decoration.add_child(TreeNode("Floral Arrangements"))
    decoration.add_child(TreeNode("Lighting Setup"))
    decoration.add_child(TreeNode("Thematic Decor"))

    
    photography.add_child(TreeNode("Traditional Photography"))
    photography.add_child(TreeNode("Candid Photography"))
    photography.add_child(TreeNode("Drone Videography"))

    
    root.add_child(catering)
    root.add_child(decoration)
    root.add_child(photography)

    return root


print("Hierarchical Tree for Wedding Vendor Marketplace:")
vendor_tree = build_vendor_tree()
vendor_tree.display_tree()
