"""Implementation of the simple graph module."""


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
        self.node_list = []
        self.edges = []

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return self.node_list

    def edges(self):
        """Return a list of all edges in the graph."""
        return self.edges

    def add_node(self, n):
        """Add a node 'n' to the graph."""
        self.node_list.append(n)

    def add_edge(self, n1, n2):
        """Add an edge to the graph with source, dest of n1, n2."""
        new_edge = Edge()
        new_edge.source = n1
        new_edge.dest = n2
        self.edges.append(new_edge)

    def del_node(self, n):
        """Delete the node n from the graph."""
        for i in self.node_list:
            if i == n:
                self.node_list.remove(n)
                return
        raise IndexError("Cannot remove node that does not exist.")

    def del_edge(self, n1, n2):
        """Delete edge from n1 to n2."""
        for i in self.edges:
            if i.source == n1 and i.dest == n2:
                self.edges.remove(i)
                return
        raise IndexError("Cannot remove edge that does not exist.")

    def has_node(self, n):
        """True or False based on if node n is contained in the graph."""
        return n in self.node_list

    def neighbors(self, n):
        """Return the list of all nodes connected to n by edges."""

    def adjacent(self, n1, n2):
        """Return True or False for if there is an edge connecting n1 and n2."""
