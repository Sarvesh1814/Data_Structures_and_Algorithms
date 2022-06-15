class BinarySearchTreeNode:
    def __init__(self,data):
        self.data= data
        self.left=None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left= BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)

        if self.right:
            elements+= self.right.in_order_traversal()
        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
        # p=self.left
        # while p:
        #     p=p.left
        # return p.data

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete_node_1(self,val):
        if val < self.data:
            if self.left:
                self.left= self.left.delete_node_1(val)
        if val>self.data:
            if self.right:
                self.right = self.right.delete_node_1(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node_1(min_val)
        return self


def build_tree(numbers):
    root=BinarySearchTreeNode(numbers[0])
    for i in range(1,len(numbers)):
        root.add_child(numbers[i])
    return root

if __name__ =="__main__":
    numbers=[17,4,1,20,9,23,18,34]
    root= build_tree(numbers)
    print(root.in_order_traversal())
    root.delete_node_1(34)
    print(root.find_max())
    
    print(root.in_order_traversal())
