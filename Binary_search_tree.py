class BinarySearchTreeNode:

    def __init__(self,data):
        self.data= data
        self.right = None
        self.left = None
    
    def add_child(self,data):
        if data == self.data:
            return
        
        if data< self.data:
            if self.left:
                self.left.add_child(data)


            else:
                self.left = BinarySearchTreeNode(data) 
        
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements=[]
        print("start",elements)
        if self.left:
            print("left ",elements)
            elements+=self.left.in_order_traversal() # here it is calling the whole function 
            # but its like the same function is written again in this line and after completing it it moves to next line
            print("end left ")
        
        elements.append(self.data) 
        print("append",elements)

        if self.right:
            print("right ",elements)
            elements+=self.right.in_order_traversal()
            print("end right ")
        print("end")
        return elements

    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()
        
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements=[self.data]
        if self.left:
            elements+=self.left.pre_order_traversal()
        
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements

    def find_min(self):
        p = self.left
        while p.left:
            p=p.left
        return p.data

    def find_max(self):
        p=self.right
        while p.right:
            p=p.right
        return p.data
    
    def calculate_sum(self):
        elements=0
        if self.left:
            elements+=self.left.calculate_sum()
        if self.right:
            elements+=self.right.calculate_sum()
        elements+=self.data
        return elements

def build_trees(elements):
    root = BinarySearchTreeNode(elements[0]) 
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root 


if __name__=="__main__":
    numbers=[17,4,1,20,9,23,18,34,88] 
    root=build_trees(numbers)
    print(root.in_order_traversal())
    print(root.post_order_traversal())
    print(root.pre_order_traversal())  
    print(root.find_min())  
    print(root.find_max())     
    print(root.calculate_sum())