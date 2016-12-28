"""Implementation of the simple graph module."""


class Node(object):
    """Edge data structure Node class."""

    def __init__(self, name=None):
        """Construct Node."""
        self.name = name


class Edge(object):
    """Edge data structure Edge class."""

    def __init__(self, source=None, dest=None):
        """Construct Edge."""
        self.source = source
        self.dest = dest


class Graph(object):
    """Edge data structure Graph class."""

    def __init__(self):
        """Construct Graph."""
        self.nodes = []
        self.edges = []

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
        new_edge = Edge()
        new_edge.source = n1
        new_edge.dest = n2
        self.edges.append(new_edge)

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
