from anytree import Node, RenderTree

A = Node("A")
B = Node("B",parent=A)
C = Node("C",parent=A)
D = Node("D",parent=B)
E = Node("E",parent=B)
F = Node("F",parent=C)
G = Node("G",parent=F)
X = Node("X",parent=C)


for pre, fill, node in RenderTree(A):
    print("%s%s" % (pre, node.name))