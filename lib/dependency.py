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
    def __init__(self, graph: Graph):
        self.nodes = graph.nodes

    def _topological_sort(self) -> List[str]:
        """
        Does a topological sort of a dependency graph.
        :return List[str]: The topological order of the dependency graph.
        """

        result = []
        zero_in_degree = []

        nodes = self.nodes
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

    def resolve(self) -> List[str]:
        """
        Returns the order for a dependency graph.
        :return List[str]: The dependency order.
        """

        order = self._topological_sort()[::-1]
        if len(order) != len(self.nodes):
            cyclic = set(self.nodes.keys()).difference(set(order))
            raise ResolverException("Cyclic dependencies detected in nodes {:s}.".format(str(cyclic)))

        return order
