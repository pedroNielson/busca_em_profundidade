#Biblioteca utilizada somente para melhor visualização do grafo

from anytree import Node, RenderTree    

A = Node("A")
B = Node("B", parent=A)
C = Node("C", parent=A)
D = Node("D", parent=B)
E = Node("E", parent=B)
F = Node("F", parent=C)
G = Node("G", parent=F)
X = Node("X", parent=C)

for pre, fill, node in RenderTree(A):
    print("%s%s" % (pre, node.name))

#Construção do grafo

class graph:

    def __init__(self, graph_dict=None):

        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

#Retorna uma lista com todos os vertices do grafo
    def verticeList(self):
        return self.graph_dict.keys()

#Encontra e retorna as arestas de um determinado vertice
    def findEdge(self, vertice):
        return self.graph_dict[vertice]

#Retorna uma lista com as arestas do grafo
    def edgeList(self):
        edges = []

        for vertices in self.graph_dict:
            for neighbours in self.graph_dict[vertices]:
                if { neighbours, vertices} not in edges:
                    edges.append({vertices, neighbours})
        return edges

#Estrutura do grafo gerado
graph_elements = {

    "a": {"c", "b"},
    "b": {"e", "d"},
    "c": {"x", "f"},
    "f": {"g"},
    "d": {},
    "e": {},
    "g": {},
    "x": {},
    
}

Graph = graph(graph_elements)

print(Graph.verticeList())
print(Graph.findEdge("c"))
print(Graph.edgeList())
