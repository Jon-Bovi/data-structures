"""Testing module for shortest path graph class."""

import pytest
from collections import OrderedDict

from data_structures import Graph


@pytest.fixture
def graph():
    """Return initialized graph."""
    return Graph()


@pytest.fixture
def complex_g(graph):
    """."""
    graph.add_edge('A', 'B', 10)
    graph.add_edge('A', 'C', 6)
    graph.add_edge('B', 'D', 3)
    graph.add_edge('B', 'E', 5)
    graph.add_edge('C', 'F', 8)
    graph.add_edge('C', 'G', 7)
    graph.add_edge('D', 'X', 4)
    graph.add_edge('D', 'Y', 9)
    graph.add_edge('E', 'B', 3)
    graph.add_edge('E', 'Z', 1)
    return graph


def test_graph_init(graph):
    """Test graph init method does what it's supposed to."""
    assert graph.node_dict == {}


def test_add_node(graph):
    """Test add_node adds node to graph."""
    graph.add_node('node')
    assert 'node' in graph.nodes()


def test_add_edge(complex_g):
    """Test that add_edge adds edge with source and dest."""
    assert len(complex_g.edges()) > 0


def test_add_edge_error(complex_g):
    """Test del_edge raises error if adds an edge that already exists."""
    with pytest.raises(ValueError):
        complex_g.add_edge('C', 'G', 1)


def test_delete_edge_error(complex_g):
    """Test del_edge raises error if edge to be deleted doesn't exist."""
    complex_g.add_edge('node', 'edon', 2)
    with pytest.raises(KeyError):
        complex_g.del_edge('node', 'noooode')


def test_del_node(complex_g):
    """Test del_node removes node."""
    complex_g.add_node('node')
    complex_g.del_node('node')
    assert 'node' not in complex_g.node_dict


def test_del_well_connected_node(graph):
    """Test del_node removes node from all edges it's part of."""
    graph.add_edge('a', 'b', 3)
    graph.add_edge('c', 'b', 33)
    graph.add_edge('a', 'c', 333)
    graph.add_edge('d', 'b', 3333)
    graph.del_node('b')
    assert 'b' not in graph.node_dict['a']
    assert 'b' not in graph.node_dict['c']
    assert 'b' not in graph.node_dict['d']


def test_del_node_error(complex_g):
    """Test del_node raises error if node to be deleted doesn't exist."""
    complex_g.add_node('mama')
    with pytest.raises(KeyError):
        complex_g.del_node('dada')


def test_del_edge(graph):
    """Test del edge removes edge."""
    graph.add_edge('node', 'edon', 0)
    graph.del_edge('node', 'edon')
    assert len(graph.edges()) == 0


def test_del_edge_error(graph):
    """Test del_edge raises error if edge to be deleted doesn't exist."""
    graph.add_edge('node', 'edon', 1.1)
    with pytest.raises(KeyError):
        graph.del_edge('node', 'noooode')


def test_has_node_true(graph):
    """Test has_node returns true if node in graph."""
    graph.add_node('mama')
    assert graph.has_node('mama')


def test_has_node_false(graph):
    """Test has_node returns false if node not in graph."""
    graph.add_node('mama')
    assert graph.has_node('dada') is False


def test_neighbors(graph):
    """Test neighbors returns all nodes connected to a single node."""
    graph.add_edge('car', 'bank', 13)
    graph.add_edge('car', 'wheels', 3)
    assert graph.neighbors('car') == OrderedDict([('bank', 13), ('wheels', 3)])


def test_neighbors_error(graph):
    """Test neighbors returns all nodes connected to a single node."""
    graph.add_edge('car', 'bank', 3)
    graph.add_edge('car', 'wheels', 3)
    with pytest.raises(KeyError):
        graph.neighbors('house') == ['bank', 'wheels']


def test_adjacent_true(graph):
    """Test adjacent returns true for nodes connected by edge."""
    graph.add_edge('beer', 'wine', 1)
    assert graph.adjacent('beer', 'wine')


def test_adjacent_false(graph):
    """Test adjacent returns false for nodes not connected by edge."""
    graph.add_node('beer')
    graph.add_node('wino')
    assert graph.adjacent('beer', 'wino') is False


def test_adjacent_reverse_is_false(graph):
    """Test adjacent returns false for nodes connected by edge in opposite direction."""
    graph.add_edge('beer', 'wine', 21)
    with pytest.raises(KeyError):
        graph.adjacent('wine', 'sake')


def test_add_duplicate_edge(graph):
    """Test add_edge raises error if edge to add already exists on graph."""
    graph.add_edge('rock', 'paper', -4)
    with pytest.raises(ValueError):
        graph.add_edge('rock', 'paper')


def test_nodes(graph):
    """Test nodes returns list of all nodes in graph."""
    graph.add_node('blah')
    graph.add_node('whamo')
    graph.add_node('zeno')
    assert 'blah' in (graph.nodes())
    assert 'whamo' in (graph.nodes())
    assert 'zeno' in (graph.nodes())


def test_nodes_no_nodes(graph):
    """Test nodes returns list of all nodes in graph even if no nodes."""
    assert graph.nodes() == []


def test_edges(graph):
    """Test edges returns list of all edges in graph."""
    graph.add_edge('blah', 'whamo', 0)
    graph.add_edge('whamo', 'blah', 1)
    graph.add_edge(2, 'whamo', 1)
    assert ('blah', 'whamo', 0) in graph.edges()
    assert ('whamo', 'blah', 1) in graph.edges()
    assert (2, 'whamo', 1) in graph.edges()


def test_edges_no_edges(graph):
    """Test edges returns list of all edges in graph even if no edges."""
    assert graph.edges() == []


def test_neighbors_of_non_existing_node(graph):
    """Test neighbors raises error when called for non-existent node."""
    with pytest.raises(KeyError):
        graph.neighbors('node')


def test_weight_existing_edge(complex_g):
    """Test weight method returns weight of an edge."""
    assert complex_g.weight('A', 'C') == 6


def test_weight_non_existing_node(complex_g):
    """Test weight raises error when looking for non-existing edge."""
    with pytest.raises(KeyError):
        complex_g.weight('anaco', 'nda')


def test_depth_non_existant_node(graph):
    """Test depth first traversal for node not in graph."""
    with pytest.raises(KeyError):
        graph.depth_first_traversal('a')


def test_depth_iterative_non_existant_node(graph):
    """Test depth first traversal for node not in graph."""
    with pytest.raises(KeyError):
        graph.depth_first_traversal_iterative('a')


def test_breadth_non_existant_node(graph):
    """Test depth first traversal for node not in graph."""
    with pytest.raises(KeyError):
        graph.breadth_first_traversal('a')


def test_depth_complex(complex_g):
    """Test the depth traversal graph."""
    res = complex_g.depth_first_traversal('A')
    assert res == list('ABDXYEZCFG')


def test_depth_iterative_complex(complex_g):
    """Test the depth traversal graph."""
    res = complex_g.depth_first_traversal_iterative('A')
    assert res == list('ABDXYEZCFG')


def test_breadth_complex(complex_g):
    """Test the breadth traversal graph."""
    res = complex_g.breadth_first_traversal('A')
    assert res == list('ABCDEFGXYZ')


def test_add_edge_depth(complex_g):
    """Test traversal after adding edge."""
    g = complex_g
    g.add_edge('B', 'C', 3)
    res = g.breadth_first_traversal('A')
    assert res == list('ABCDEFGXYZ')


def test_shortest_dijkstra(complex_g):
    """Test dijkstra returns shortest path."""
    assert complex_g.dijkstra('A', 'F') == ['F', 'C', 'A']


def test_shortest_dijkstra_long(complex_g):
    """Test dijkstra returns shortest path."""
    assert complex_g.dijkstra('A', 'X') == ['X', 'D', 'B', 'A']


def test_loop_dijkstra(complex_g):
    """Test dijkstra returns shortest path."""
    assert complex_g.dijkstra('A', 'Z') == ['Z', 'E', 'B', 'A']


def test_floyd_warshall_no_path(complex_g):
    """Test fw returns empty list if there's no path between nodes."""
    path, distances = complex_g.floyd_warshall()
    assert complex_g.floyd_warshall_path(path, 'Z', 'A') == []


def test_floyd_warshall(complex_g):
    """Floyd warshall should return all shortest paths."""
    path, distances = complex_g.floyd_warshall()
    assert complex_g.floyd_warshall_path(path, 'A', 'Z') == ['A', 'B', 'E', 'Z']
    assert complex_g.floyd_warshall_path(path, 'A', 'F') == ['A', 'C', 'F']
    assert complex_g.floyd_warshall_path(path, 'A', 'X') == ['A', 'B', 'D', 'X']
    assert distances['A']['Z'] == 16
    assert distances['A']['F'] == 14
    assert distances['A']['X'] == 17


def test_alternative_routes(complex_g):
    """Test fw with a graph with multiple alternative routes."""
    complex_g.add_edge('C', 'B', 1)
    complex_g.add_edge('A', 'X', 20)
    path, distances = complex_g.floyd_warshall()
    assert complex_g.floyd_warshall_path(path, 'A', 'B') == ['A', 'C', 'B']
    assert complex_g.floyd_warshall_path(path, 'A', 'X') == ['A', 'C', 'B', 'D', 'X']
    assert complex_g.dijkstra('A', 'B') == ['B', 'C', 'A']
    assert complex_g.dijkstra('A', 'X') == ['X', 'D', 'B', 'C', 'A']