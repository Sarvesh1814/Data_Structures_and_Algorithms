#Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.

class TreeNode:

    def __init__(self,data):
        self.parent= None
        self.children = []
        self.data = data
        # self.data["Designation"] = data[1]
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p= self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_Tree1(self,type_tree):

        prefix= " " * self.get_level() * 3 + "|__" if self.parent else ""
        if type_tree == "Both":
            print(prefix +self.data[0]+" ("+ self.data[1]+")")
        elif type_tree == "Name":
            print(prefix+self.data[0])
        elif type_tree == "Designation":
            print(prefix+"("+ self.data[1]+")")
        
        if self.children:
            for child in self.children:
                child.print_Tree1(type_tree)

def build_company():
    ceo= TreeNode(["Nilupul","CEO"])

    cto = TreeNode(["Chinmay","CTO"])
    IH= TreeNode(["Vishwa","Infrastructure Head"])
    CM = TreeNode(["Dhaval","Cloud Manager"])
    AM = TreeNode(["Abhijit","App Manager"])
    AH = TreeNode(["Aamir","Application Head"])

    IH.add_child(CM)
    IH.add_child(AM)
    
    cto.add_child(IH)
    cto.add_child(AH)

    HR = TreeNode(["Gels","HR Head"])
    HR.add_child(TreeNode(["Peter","Recruitment Manager"]))
    HR.add_child(TreeNode(["Waqas","Policy Manager"]))

    ceo.add_child(cto)
    ceo.add_child(HR)

    return ceo

if __name__ == "__main__":
    cc= build_company()
    print("By Names")
    cc.print_Tree1("Name")
    print("     ")
    print("By Designation")
    cc.print_Tree1("Designation")
    print("     ")
    print("By Both")
    cc.print_Tree1("Both")





