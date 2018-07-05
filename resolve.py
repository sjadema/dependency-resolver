from lib.dependency import Node, Graph, Resolver

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

#   a       g
#  / \     / \
# b   c   h   i
#      \
#       d
#      /  \
#     e    f

b.add_edge(a)
c.add_edge(a)
d.add_edge(c)
e.add_edge(d)
f.add_edge(d)
h.add_edge(g)
i.add_edge(g)

graph = Graph()
graph.add_node(a)
graph.add_node(b)
graph.add_node(c)
graph.add_node(d)
graph.add_node(e)
graph.add_node(f)
graph.add_node(g)
graph.add_node(h)
graph.add_node(i)

print(Resolver.get_order(graph))
