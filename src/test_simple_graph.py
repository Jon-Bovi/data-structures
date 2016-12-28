"""Test simple graph module."""
import pytest


@pytest.fixture
def node():
    """Return node."""
    from simple_graph import Node
    return Node()


@pytest.fixture
def another_node():
    """Return another_node."""
    from simple_graph import Node
    return Node()


@pytest.fixture
def edge(node, another_node):
    """Return an edge object."""
    from simple_graph import Edge
    return Edge(node, another_node)


@pytest.fixture
def graph():
    """Return initialized graph."""
    from simple_graph import Graph
    return Graph()


def test_node_init(node):
    """Test node init method does what it's supposed to."""
    assert node.name is None


def test_edge_init(edge):
    """Test edge init method does what it's supposed to."""
    from simple_graph import Node
    assert type(edge.source) is Node
    assert type(edge.dest) is Node


def test_graph_init(graph):
    """Test graph init method does what it's supposed to."""
    assert graph.nodes == []
    assert graph.edges == []


def test_add_node(graph, node):
    """Test add_node adds node to graph."""
    graph.add_node(node)
    assert node in graph.nodes


def test_add_edge(graph, node, another_node):
    """Test that add_edge adds edge with source and dest."""
    graph.add_edge(node, another_node)
    assert graph.edges[0].source is node
    assert graph.edges[0].dest is another_node
