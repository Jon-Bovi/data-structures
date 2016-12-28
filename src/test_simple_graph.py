"""Test simple graph module."""
import pytest


@pytest.fixture
def edge():
    """Return an edge object."""
    from simple_graph import Edge
    return Edge('node', 'another_node')


@pytest.fixture
def graph():
    """Return initialized graph."""
    from simple_graph import Graph
    return Graph()


def test_edge_init(edge):
    """Test edge init method does what it's supposed to."""
    assert edge.source == 'node'
    assert edge.dest == 'another_node'


def test_graph_init(graph):
    """Test graph init method does what it's supposed to."""
    assert graph.node_list == []
    assert graph.edges == []


def test_add_node(graph):
    """Test add_node adds node to graph."""
    graph.add_node('node')
    assert 'node' in graph.node_list


def test_add_edge(graph):
    """Test that add_edge adds edge with source and dest."""
    graph.add_edge('node', 'another_node')
    assert graph.edges[0].source == 'node'
    assert graph.edges[0].dest == 'another_node'


def test_del_node(graph):
    """."""
    graph.add_node('node')
    graph.del_node('node')
    assert 'node' not in graph.node_list


def test_del_node_error(graph):
    """."""
    graph.add_node('mama')
    with pytest.raises(IndexError):
        graph.del_node('dada')


def test_del_edge(graph):
    """."""
    graph.add_edge('node', 'edon')
    graph.del_edge('node', 'edon')
    assert len(graph.edges) == 0


def test_del_edge_error(graph):
    """."""
    graph.add_edge('node', 'edon')
    with pytest.raises(IndexError):
        graph.del_edge('node', 'noooode')


def test_has_node_true(graph):
    """."""
    graph.add_node('mama')
    assert graph.has_node('mama')


def test_has_node_false(graph):
    """."""
    graph.add_node('mama')
    assert graph.has_node('dada') is False


def test_neighbors(graph):
    """."""
    graph.add_edge('bank', 'car')
    graph.add_edge('wheels', 'car')
    assert graph.neighbors('car') == ['bank', 'wheels']


def test_adjacent(graph):
    """."""
    graph.add_edge('beer', 'wine')
    assert graph.adjacent('beer', 'wine')
    assert graph.adjacent('wine', 'beer')
