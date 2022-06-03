class TreeNode:

    def __init__(self,data):
        self.parent = None
        self.children = []
        self.data = data 

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level=0 
        p = self.parent
        while p:
            level+=1
            p=p.parent
        return level 

    def print_tree(self,levels=0):
        prefix = ' ' * self.get_level() * 5 + "|__" if self.parent else ''
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                if self.get_level()<levels:
                    child.print_tree(levels)
                    
                     
    
def build_global():

    gb = TreeNode("Global")


    Ind = TreeNode("India")
    
    GJ = TreeNode("Gujarat")
    GJ.add_child(TreeNode("Ahmedabad"))
    GJ.add_child(TreeNode("Baroda"))

    KA= TreeNode("Karnataka")
    KA.add_child(TreeNode("Bangluru"))
    KA.add_child(TreeNode("Mysore"))

    Ind.add_child(GJ)
    Ind.add_child(KA)


    USA= TreeNode("USA")
    
    NJ= TreeNode("New Jersy")
    NJ.add_child(TreeNode("Princeton"))
    NJ.add_child(TreeNode("Trenton"))

    CF= TreeNode("California")
    CF.add_child(TreeNode("San Francisco"))
    CF.add_child(TreeNode("Mountain View"))
    CF.add_child(TreeNode("Palo Alto"))

    USA.add_child(NJ)
    USA.add_child(CF)

    gb.add_child(Ind)
    gb.add_child(USA)

    return gb

if __name__ == "__main__":
    gg= build_global()
    gg.print_tree(1)

 


