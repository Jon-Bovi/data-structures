"""Module with implementation of Weighted Graph."""

import sys
from collections import defaultdict
from data_structures import Queue, BinaryHeap


class Graph(object):
    """Graph data structure."""

    def __init__(self):
        """Initialize graph."""
        self.node_dict = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.node_dict.keys())

    def edges(self):
        """Return a list of all edges in the graph."""
        return [
            (n1, n2, w)
            for n1, edges in self.node_dict.items()
            for n2, w in edges.items()
        ]

    def add_node(self, n):
        """Add node n to the graph."""
        self.node_dict.setdefault(n, {})

    def add_edge(self, n1, n2, weight=0):
        """
        Add an edge to the graph from n1 to n2, weight optional.

        Add nodes if not already in graph.
        """
        self.add_node(n1)
        self.add_node(n2)
        if n2 in self.node_dict[n1]:
            raise ValueError("Edge already exists")
        self.node_dict[n1][n2] = weight

    def del_node(self, n):
        """Delete node n from the graph. Raise error if no such node exists."""
        if n in self.node_dict:
            del self.node_dict[n]
            for node in self.node_dict:
                try:
                    self.del_edge(node, n)
                except:
                    pass
        else:
            raise KeyError("Cannot remove node that does not exist.")

    def del_edge(self, n1, n2):
        """Delete edge from n1 to n2. Raise error if no such edge exists."""
        try:
            del self.node_dict[n1][n2]
        except KeyError:
            raise KeyError("Cannot remove edge that does not exist.")

    def has_node(self, n):
        """Return whether node n is in graph."""
        return n in self.node_dict

    def neighbors(self, n):
        """
        Return the list of all nodes connected to node n.

        Raise error if n is not present.
        """
        if n not in self.node_dict:
            raise KeyError("Cannot return neighbors of node that does not exist.")
        return self.node_dict[n]

    def adjacent(self, n1, n2):
        """
        Return True/False for if an edge connects nodes n1 and n2.

        Raise error if either nodes not present.
        """
        if n1 in self.node_dict and n2 in self.node_dict:
            return n2 in self.node_dict[n1]
        raise KeyError("Nodes not in graph.")

    def __getitem__(self, item):
        return self.neighbors(item)

    def weight(self, n1, n2):
        """Return weight of an edge."""
        try:
            return self.node_dict[n1][n2]
        except KeyError:
            raise KeyError("Nodes not in graph.")

    def depth_first_traversal(self, start):
        """Traverse graph depth first."""
        if start not in self.node_dict:
            raise KeyError(str(start) + ' not in graph')

        def depth_recurse(from_, visited):
            res = [from_]
            visited.add(from_)
            for node in list(self.node_dict[from_]), len(self.node_dict[from_]):
                if node not in visited:
                    res += depth_recurse(node, visited)
            return res

        return depth_recurse(start, set())

    def depth_first_traversal_iterative(self, start):
        """Iteratively traverse graph depth first."""
        if start not in self.node_dict:
            raise KeyError(str(start) + ' not in graph')
        res, stack, visited = [], [start], set()
        while stack:
            cur_node = stack.pop()
            if cur_node not in visited:
                res.append(cur_node)
                visited.add(cur_node)
                for node in self.node_dict[cur_node]:
                    if node not in visited:
                        stack.append(node)
        return res

    def breadth_first_traversal(self, start):
        """Iteratively traverse graph breadth first."""
        if start not in self.node_dict:
            raise KeyError(str(start) + ' not in graph')
        res, queue, visited = [], Queue([start]), {start}
        while queue.head:
            cur_node = queue.dequeue()
            res.append(cur_node)
            for node in self.node_dict[cur_node]:
                if node not in visited:
                    visited.add(node)
                    queue.enqueue(node)
        return res

    def dijkstra(self, start, end):
        """Find shortest path between start and end via Dijkstra's algorithm."""
        previous, unvisited = {}, BinaryHeap([(0, start)])
        distance = defaultdict(lambda: float('inf'))
        distance[start] = 0
        while True:
            try:
                dist, node = unvisited.pop()
            except IndexError:
                break
            if distance[node] > distance[end]:
                break
            for neighbor in self.neighbors(node):
                alt_path = distance[node] + self.weight(node, neighbor)
                if alt_path < distance[neighbor]:
                    distance[neighbor] = alt_path
                    previous[neighbor] = node
                    unvisited.push((distance[neighbor], neighbor))
        result = []
        result.append(end)
        curr = end
        while curr in previous:
            result.append(previous[curr])
            curr = previous[curr]
        return result[::-1], distance[end]

    def floyd_warshall(self):
        """Find all shortest paths and distances via floyd-warshall alg."""
        distance = {}
        path_dict = {}
        for from_node in self.nodes():
            distance[from_node] = {}
            path_dict[from_node] = {}
            for node in self.nodes():
                distance[from_node][node] = float('inf')
                path_dict[from_node][node] = None
            distance[from_node][from_node] = 0
            neighbors = self.neighbors(from_node)
            for neighbor in neighbors:
                distance[from_node][neighbor] = neighbors[neighbor]
                path_dict[from_node][neighbor] = neighbor
        for k in self.nodes():
            for i in self.nodes():
                for j in self.nodes():
                    if distance[i][k] + distance[k][j] < distance[i][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                        path_dict[i][j] = path_dict[i][k]
        return path_dict, distance

    def floyd_warshall_path(self, path_dict, start, end):
        """Return shortest path between start and end via floyd-warshall algorithm."""
        if path_dict[start][end] is None:
            return []
        path = [start]
        while start != end:
            start = path_dict[start][end]
            path.append(start)
        return path

    @classmethod
    def from_dict(cls, gdict):
        from itertools import chain, repeat
        inst = cls()
        try:
            for fr, (to, w) in chain(*(zip(repeat(k), v.items()) for k, v in gdict.items())):
                inst.add_edge(fr, to, w)
        except AttributeError:
            for fr, to in chain(*(zip(repeat(k), v) for k, v in gdict.items())):
                inst.add_edge(fr, to)
        return inst


if __name__ == '__main__':  # pragma: no cover
    import random

    graph = Graph()
    for i in range(100):
        try:
            graph.add_edge(random.randint(0, 20),
                           random.randint(0, 20),
                           random.randint(0, 5))
        except:
            pass

    if len(sys.argv) > 1 and sys.argv[1] == 'timeit':
        import timeit
        from pprint import pprint

        start = graph.nodes()[random.randint(0, len(graph.nodes()))]

        pprint(graph.node_dict)

        depth = timeit.timeit(
            stmt="graph.depth_first_traversal(start)",
            setup="from __main__ import graph, start",
            number=1000,
        )
        depth_i = timeit.timeit(
            stmt="graph.depth_first_traversal_iterative(start)",
            setup="from __main__ import graph, start",
            number=1000,
        )
        breadth = timeit.timeit(
            stmt="graph.breadth_first_traversal(start)",
            setup="from __main__ import graph, start",
            number=1000,
        )
        print('\n1000 recursive depth first traversals:\n\t{} seconds\n'.format(depth) +
              '\tPath: {}\n'.format(graph.depth_first_traversal(start)) +
              '\n1000 iterative depth first traversals:\n\t{} seconds\n'.format(depth_i) +
              '\tPath: {}\n'.format(graph.depth_first_traversal_iterative(start)) +
              '\n1000 breadth first traversals:\n\t{} seconds\n'.format(breadth) +
              '\tPath: {}\n'.format(graph.breadth_first_traversal(start)))
