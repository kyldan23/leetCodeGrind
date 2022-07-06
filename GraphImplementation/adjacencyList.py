class Graph: 
    def __init__(self, nodes): 
        self.nodes = nodes 
class Node: 
    def __init__(self, val, children):
        self.val = val
        self.children = children