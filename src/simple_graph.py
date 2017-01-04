"""Implementation of the simple graph module."""


class Edge(object):
    """Edge data structure Edge class."""

    def __init__(self, source=None, dest=None):
        """Construct Edge."""
        self.source = source
        self.dest = dest

    def __repr__(self):
        """Return readable representation of edge."""
        a, b = self.source, self.dest
        if type(a) is str:
            a = "'" + a + "'"
        if type(b) is str:
            b = "'" + b + "'"
        return "({}, {})".format(a, b)


class Graph(object):
    """Edge data structure Graph class."""

    def __init__(self):
        """Construct Graph."""
        self.node_list = []
        self.edge_list = []

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return self.node_list

    def edges(self):
        """Return a list of all edges in the graph."""
        return self.edge_list

    def add_node(self, n):
        """Add a node 'n' to the graph."""
        self.node_list.append(n)

    def add_edge(self, n1, n2):
        """Add an edge to the graph with source, dest of 'n1', 'n2'. Add node if either not present."""
        if n1 not in self.node_list:
            self.add_node(n1)
        if n2 not in self.node_list:
            self.add_node(n2)
        if not self.adjacent(n1, n2):
            self.edge_list.append(Edge(n1, n2))
        else:
            raise ValueError("Cannot add edge that already exists.")

    def del_node(self, n):
        """Delete the node 'n' from the graph. Raise error if no such node exists."""
        for i in self.node_list:
            if i == n:
                self.node_list.remove(n)
                return
        raise IndexError("Cannot remove node that does not exist.")

    def del_edge(self, n1, n2):
        """Delete edge from 'n1' to 'n2'. Raise error if no such edge exists."""
        for i in self.edge_list:
            if i.source == n1 and i.dest == n2:
                self.edge_list.remove(i)
                return
        raise IndexError("Cannot remove edge that does not exist.")

    def has_node(self, n):
        """True or False based on if node 'n' is present in the graph."""
        return n in self.node_list

    def neighbors(self, n):
        """Return the list of all nodes connected to 'n' by edges. Raise error if n is not present."""
        edge_sources = []
        if n not in self.node_list:
            raise IndexError("Cannot return neighbors of node that does not exist.")
        for i in self.edge_list:
            if i.dest == n:
                edge_sources.append(i.source)
        return edge_sources

    def adjacent(self, n1, n2):
        """Return True/False for if an edge connects 'n1' and 'n2'. Raises error if either nodes not present."""
        for i in self.edge_list:
            if i.source == n1 and i.dest == n2:
                return True
        return False
