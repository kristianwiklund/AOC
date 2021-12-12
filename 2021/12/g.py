class Graph:

    nodes = {}
    def add_edge(self, a,b):
        if a in self.nodes:
            self.nodes[a].add(b)
        else:
            self.nodes[a] = {b}

        if b in self.nodes:
            self.nodes[b].add(a)
        else:
            self.nodes[b] = {a}

    def neighbors(self, a):

        if a in self.nodes:
            return self.nodes[a]
        else:
            return set()
        
    def __repr__(self):
        return str(self.nodes)
