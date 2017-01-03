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
            raise KeyError("Cannot remove node that does not exist.")

    def del_edge(self, n1, n2):
        """Delete edge from 'n1' to 'n2'. Raise error if no such edge exists."""
        if n1 in self.node_dict and n2 in self.node_dict[n1]:
            self.node_dict[n1].remove(n2)
        else:
            raise KeyError("Cannot remove edge that does not exist.")

    def has_node(self, n):
        """True or False based on if node 'n' is present in the graph."""
        return n in self.node_dict

    def neighbors(self, n):
        """Return the list of all nodes connected to 'n' by edges. Raise error if n is not present."""
        if n not in self.node_dict:
            raise KeyError("Cannot return neighbors of node that does not exist.")
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
        try:
            for n in self.node_dict[start]:
                if n not in track:
                    res += self.depth_first_traversal(n, track)
        except KeyError:
            raise KeyError(str(start) + ' not in graph')
        return res

    def breadth_first_traversal(self, start):
        """Breadth version of graph traversal."""
        try:
            res = [start]
            queue = Queue(res)
            track = set(res)
            while queue:
                children = self.node_dict[queue.dequeue()]
                for child in children:
                    if child not in track:
                        queue.enqueue(child)
                        track.add(child)
                        res.append(child)
        except KeyError:
            raise KeyError(str(start) + ' not in graph')
        return res

    def depth_first_traversal_iterative(self, start):
        """Breadth version of graph traversal."""
        try:
            res = []
            stack = Stack([start])
            track = set([start])
            while stack:
                cur_node = stack.pop()
                children = reversed(self.node_dict[cur_node])
                for child in children:
                    if child not in track:
                        stack.push(child)
                        track.add(child)
                res.append(cur_node)
        except KeyError:
            raise KeyError(str(start) + ' not in graph')
        return res


if __name__ == '__main__': # pragma: no cover
    import timeit
    import random

    def complex_g():
        """Return a somewhat convoluted graph."""
        graph = Graph()
        for i in range(100):
            try:
                graph.add_edge(random.randint(0, 30), random.randint(31, 60))
            except:
                pass
        return graph

    depth = timeit.timeit(
        stmt="graph=complex_g(); graph.depth_first_traversal(graph.nodes()[0])",
        setup="from __main__ import complex_g",
        number=1000,
    )
    depth_i = timeit.timeit(
        stmt="graph=complex_g(); graph.depth_first_traversal_iterative(graph.nodes()[0])",
        setup="from __main__ import complex_g",
        number=1000,
    )
    breadth = timeit.timeit(
        stmt="graph=complex_g(); graph.breadth_first_traversal(graph.nodes()[0])",
        setup="from __main__ import complex_g",
        number=1000,
    )

    print('1000 depth first traversals:\n\t{} seconds\n'.format(depth) +
          '1000 iterative depth first traversals:\n\t{} seconds\n'.format(depth_i) +
          '1000 breadth first traversals:\n\t{} seconds\n'.format(breadth))
