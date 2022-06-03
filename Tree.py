
class TreeNode:

    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level=level+1
            p=p.parent
        return level

    def print_tree(self):
        prefix= " " * self.get_level() * 3 + "|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    
def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Gaming Pad"))
    laptop.add_child(TreeNode("IdeaPad"))

    mobile = TreeNode("Mobile")
    mobile.add_child(TreeNode("Iphone"))
    mobile.add_child(TreeNode("Samsung"))
    mobile.add_child(TreeNode("Vivo"))

    Tv= TreeNode("TV")
    Tv.add_child(TreeNode("Sony"))
    Tv.add_child(TreeNode("Samsung T"))
    Tv.add_child(TreeNode("Mi"))

    Headphones= TreeNode("Headphone")
    boat= TreeNode("BoAT")
    boat.add_child(TreeNode("Rockers"))
    
    Headphones.add_child(boat)

    root.add_child(laptop)
    root.add_child(Tv)
    root.add_child(mobile)
    root.add_child(Headphones)

    return root



    




if __name__ == "__main__":
    tree = build_product_tree()
    tree.print_tree()
    pass