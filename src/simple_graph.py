"""Implementation of the simple graph module."""


class Node:
    """Edge data structure Node class."""

    name = None


class Edge:
    """Edge data structure Edge class."""

    source = None
    dest = None


class Graph:
    """Edge data structure Graph class."""

    nodes = []
    edges = []

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return self.nodes

    def edges(self):
        """Return a list of all edges in the graph."""
        return self.edges

    def add_node(self, n):
        """Add a node 'n' to the graph."""
        new_node = Node()
        new_node.name = n
        self.nodes.append(n)

    def add_edge(self, n1, n2):
        """Add an edge to the graph with source, dest of n1, n2."""

    def del_node(self, n):
        """Delete the node n from the graph."""

    def del_edge(self, n1, n2):
        """Delete edge from n1 to n2."""

    def has_node(self, n):
        """True or False based on if node n is contained in the graph."""

    def neighbors(self, n):
        """Return the list of all nodes connected to n by edges."""

    def adjacent(self, n1, n2):
        """Return True or False for if there is an edge connecting n1 and n2."""
