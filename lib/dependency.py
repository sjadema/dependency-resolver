from typing import List


class Node:
    def __init__(self, name: str):
        self.name = name
        self.edges = []

    def add_edge(self, node: 'Node'):
        self.edges.append(node)

    def __repr__(self):
        return self.name


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, edge: Node) -> None:
        """
        Adds an edge to the node.
        :param Node edge: The edge to add.
        """

        if edge.name not in self.nodes:
            self.nodes[edge.name] = edge


class ResolverException(Exception):
    pass


class Resolver:
    @staticmethod
    def topological_sort(graph: Graph) -> List[str]:
        """
        Does a topological sort of a dependency graph.
        :param Graph graph: The graph to sort.
        :return List[str]: The topological order of the dependency graph.
        """

        result = []
        zero_in_degree = []

        nodes = graph.nodes
        in_degree = {node: 0 for node in nodes}

        for node in nodes:
            for edge in nodes[node].edges:
                in_degree[edge.name] += 1

        for d in in_degree:
            if in_degree[d] == 0:
                zero_in_degree.append(d)

        while zero_in_degree:
            n = zero_in_degree.pop(0)
            result.append(n)

            for edge in nodes[n].edges:
                in_degree[edge.name] -= 1
                if in_degree[edge.name] == 0:
                    zero_in_degree.append(edge.name)

        return result

    @staticmethod
    def get_order(graph: Graph) -> List[str]:
        """
        Returns the order for a dependency graph.
        :param Graph graph: The graph to get the order for.
        :return List[str]: The dependency order.
        """

        order = Resolver.topological_sort(graph)[::-1]
        if len(order) != len(graph.nodes):
            cyclic = set(graph.nodes.keys()).difference(set(order))
            raise ResolverException("Cyclic dependencies detected in nodes {:s}.".format(str(cyclic)))

        return order
