from sysconfig import get_paths
import time
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        # print(self.graph_dict)

    def get_paths(self,start,end,path=[]):
        path = path+[start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node,end,path)
                paths= paths+new_paths
        return paths 
    
    def shortest_path(self,start,end,path=[]):
        path=path+[start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp= self.shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

    
                    
                    




    
if __name__ =="__main__":
    edges= [("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")]
    root = Graph(edges)
    print("Available Paths: ",root.get_paths(end="Toronto",start="Mumbai"))
    print("                     ")
    print("Shortest Path: ",root.shortest_path(end="Toronto",start="Mumbai"))
    
    

