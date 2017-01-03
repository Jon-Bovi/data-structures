"""Module with implementation of Graph Traversal."""
from queue import Queue
from stack import Stack


class Graph(object):
    """Implementation of Graph Traversal."""

    def __init__(self):
        """."""
        self.node_dict = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.node_dict.keys())

    def edges(self):
        """Return a list of all edges in the graph."""
        edge_list = []
        for node1 in self.node_dict:
            for node2 in self.node_dict[node1]:
                edge_list.append((node1, node2))
        return edge_list

    def add_node(self, n):
        """Add a node 'n' to the graph."""
        self.node_dict.setdefault(n, [])

    def add_edge(self, n1, n2):
        """Add an edge to the graph with source, dest of 'n1', 'n2'. Add node if either not present."""
        self.add_node(n1)
        self.add_node(n2)
        if n2 in self.node_dict[n1]:
            raise ValueError("Edge already exists")
        self.node_dict[n1].append(n2)

    def del_node(self, n):
        """Delete the node 'n' from the graph. Raise error if no such node exists."""
        if n in self.node_dict:
            del self.node_dict[n]
        else:
            raise IndexError("Cannot remove node that does not exist.")

    def del_edge(self, n1, n2):
        """Delete edge from 'n1' to 'n2'. Raise error if no such edge exists."""
        if n1 in self.node_dict and n2 in self.node_dict[n1]:
            self.node_dict[n1].remove(n2)
        else:
            raise IndexError("Cannot remove edge that does not exist.")

    def has_node(self, n):
        """True or False based on if node 'n' is present in the graph."""
        return n in self.node_dict

    def neighbors(self, n):
        """Return the list of all nodes connected to 'n' by edges. Raise error if n is not present."""
        if n not in self.node_dict:
            raise IndexError("Cannot return neighbors of node that does not exist.")
        return self.node_dict[n]

    def adjacent(self, n1, n2):
        """Return True/False for if an edge connects 'n1' and 'n2'. Raises error if either nodes not present."""
        if n1 in self.node_dict and n2 in self.node_dict:
            return n2 in self.node_dict[n1]
        raise KeyError("Nodes not in graph!")

    def depth_first_traversal(self, start, track=None):
        """Graph traversal depth first."""
        res = [start]
        if track is None:
            track = set()
        track.add(start)
        for n in self.node_dict[start]:
            if n not in track:
                res += self.depth_first_traversal(n, track)
        return res

    def breadth_first_traversal(self, start, track=None):
        """Breadth version of graph traversal."""
        res = [start]
        queue = Queue(res)
        track = set(start)
        while queue:
            children = self.node_dict[queue.dequeue()]
            for child in children:
                if child not in track:
                    queue.enqueue(child)
                    track.add(child)
                    res.append(child)
        return res

    def depth_first_traversal_iterative(self, start, track=None):
        """Breadth version of graph traversal."""
        res = [start]
        stack = Stack(res)
        track = set(start)
        while stack:
            children = self.node_dict[stack.pop()]
            for child in children:
                if child not in track:
                    stack.push(child)
                    track.add(child)
                    res.append(child)
        return res


if __name__ == '__main__':
    import timeit

    def complex_g():
        """Return a somewhat convoluted graph."""
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('B', 'E')
        graph.add_edge('D', 'H')
        graph.add_edge('D', 'I')
        graph.add_edge('E', 'J')
        graph.add_edge('E', 'K')
        graph.add_edge('C', 'F')
        graph.add_edge('C', 'G')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'A')
        return graph

    depth = timeit.timeit(
        stmt="complex_g().depth_first_traversal",
        setup="from __main__ import complex_g",
        number=100000,
        repeat=3
    )
    breadth = timeit.timeit(
        stmt="complex_g().breadth_first_traversal",
        setup="from __main__ import complex_g",
        number=100000,
        repeat=3
    )

    print('100,000 depth first traversals:\n\t{} seconds\n'.format(depth) +
          '\tPath: {}\n'.format(complex_g().depth_first_traversal('A')) +
          '100,000 breadth first traversals:\n\t{} seconds\n'.format(breadth) +
          '\tPath: {}'.format(complex_g().breadth_first_traversal('A')))
