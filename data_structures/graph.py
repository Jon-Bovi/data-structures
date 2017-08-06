"""Module with implementation of Weighted Graph."""

import sys
from collections import OrderedDict

from data_structures import Queue, Stack


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
        edge_list = []
        for node1 in self.node_dict:
            for node2 in self.node_dict[node1]:
                edge_list.append((node1,
                                  node2,
                                  self.node_dict[node1][node2]))
        return edge_list

    def add_node(self, n):
        """Add node n to the graph."""
        self.node_dict.setdefault(n, OrderedDict())

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
        if n1 in self.node_dict and n2 in self.node_dict[n1]:
            del self.node_dict[n1][n2]
        else:
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

    def weight(self, n1, n2):
        """Return weight of an edge."""
        try:
            return self.node_dict[n1][n2]
        except KeyError:
            raise KeyError("Nodes not in graph.")

    def depth_first_traversal(self, start, visited=None):
        """Traverse graph depth first."""
        res = [start]
        if visited is None:
            visited = set()
        visited.add(start)
        try:
            for n in self.node_dict[start]:
                if n not in visited:
                    res += self.depth_first_traversal(n, visited)
        except KeyError:
            raise KeyError(str(start) + ' not in graph')
        return res

    def breadth_first_traversal(self, start):
        """Iteratively traverse graph breadth first."""
        try:
            res = []
            queue = Queue([start])
            visited = set()
            while queue.head:
                cur_node = queue.dequeue()
                if cur_node not in visited:
                    res.append(cur_node)
                    visited.add(cur_node)
                    for child in self.node_dict[cur_node]:
                        queue.enqueue(child)
        except KeyError:
            raise KeyError(str(start) + ' not in graph')
        return res

    def depth_first_traversal_iterative(self, start):
        """Iteratively traverse graph depth first."""
        try:
            res = []
            stack = Stack([start])
            visited = set()
            while stack.top:
                cur_node = stack.pop()
                if cur_node not in visited:
                    res.append(cur_node)
                    visited.add(cur_node)
                    for child in reversed(self.node_dict[cur_node]):
                        stack.push(child)
        except KeyError:
            raise KeyError(str(start) + ' not in graph')
        return res

    def dijkstra(self, start, end):
        """Find shortest path between start and end via Dijkstra's algorithm."""
        unvisited = self.nodes()
        distance = {}
        previous = {}
        for node in unvisited:
            distance[node] = sys.maxsize
        distance[start] = 0
        while len(unvisited) > 0:
            node = unvisited[0]
            smallest_curr = sys.maxsize
            for d in distance:
                if d in unvisited and distance[d] < smallest_curr:
                    node = d
                    smallest_curr = distance[d]
            unvisited.remove(node)
            for neighbor in self.neighbors(node).keys():
                alt_path = distance[node] + self.weight(node, neighbor)
                if alt_path < distance[neighbor]:
                    distance[neighbor] = alt_path
                    previous[neighbor] = node
        result = []
        result.append(end)
        curr = end
        while curr in previous:
            result.append(previous[curr])
            curr = previous[curr]
        return result

    def floyd_warshall(self):
        """Find all shortest paths and distances via floyd-warshall alg."""
        distance = {}
        path_dict = {}
        for from_node in self.nodes():
            distance[from_node] = {}
            path_dict[from_node] = {}
            for node in self.nodes():
                distance[from_node][node] = sys.maxsize
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
