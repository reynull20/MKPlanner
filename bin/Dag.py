# GRAPH

class DAG:
    nodes = []
    edge = []

    def __init__(self, prec):
        node_list = []
        edge_list = []
        for course in prec:
            if(course not in node_list):
                node_list.append(course)
            for j in prec[course]:
                edge_list.append([j, course])
        self.nodes = node_list
        self.edge = edge_list
                
    def getnodes(self):
        return self.nodes

    def getedge(self):
        return self.edge

    def getderajatmasuk(self):
        in_node = {}
        for course in self.nodes:
            count = 0
            for i in self.edge:
                if(i[1] == course):
                    count += 1
            in_node[course] = count
            
        return in_node
            
        
