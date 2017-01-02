"""Test simple graph module."""
import pytest


@pytest.fixture
def graph():
    """Return initialized graph."""
    from graph import Graph
    return Graph()


@pytest.fixture
def complex_g(graph):
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('D', 'X')
    graph.add_edge('D', 'Y')
    graph.add_edge('E', 'Z')
    graph.add_edge('E', '1')
    graph.add_edge('C', 'F')
    graph.add_edge('C', 'G')
    return graph


def test_graph_init(graph):
    """Test graph init method does what it's supposed to."""
    assert graph.node_dict == {}


def test_add_node(graph):
    """Test add_node adds node to graph."""
    graph.add_node('node')
    assert 'node' in graph.node_dict


# def test_add_edge(graph):
#     """Test that add_edge adds edge with source and dest."""
#     graph.add_edge('node', 'another_node')
#     assert graph.edge_list[0].source == 'node'
#     assert graph.edge_list[0].dest == 'another_node'


# def test_del_node(graph):
#     """Test del_node removes node."""
#     graph.add_node('node')
#     graph.del_node('node')
#     assert 'node' not in graph.node_list


# def test_del_node_error(graph):
#     """Test del_node raises error if node to be deleted doesn't exist."""
#     graph.add_node('mama')
#     with pytest.raises(IndexError):
#         graph.del_node('dada')


# def test_del_edge(graph):
#     """Test del edge removes edge."""
#     graph.add_edge('node', 'edon')
#     graph.del_edge('node', 'edon')
#     assert len(graph.edge_list) == 0


# def test_del_edge_error(graph):
#     """Test del_edge raises error if edge to be deleted doesn't exist."""
#     graph.add_edge('node', 'edon')
#     with pytest.raises(IndexError):
#         graph.del_edge('node', 'noooode')


# def test_has_node_true(graph):
#     """Test has_node returns true if node in graph."""
#     graph.add_node('mama')
#     assert graph.has_node('mama')


# def test_has_node_false(graph):
#     """Test has_node returns false if node not in graph."""
#     graph.add_node('mama')
#     assert graph.has_node('dada') is False


# def test_neighbors(graph):
#     """Test neighbors returns all nodes connected to a single node."""
#     graph.add_edge('bank', 'car')
#     graph.add_edge('wheels', 'car')
#     assert graph.neighbors('car') == ['bank', 'wheels']


# def test_adjacent_true(graph):
#     """Test adjacent returns true for nodes connected by edge."""
#     graph.add_edge('beer', 'wine')
#     assert graph.adjacent('beer', 'wine')


# def test_adjacent_false(graph):
#     """Test adjacent returns false for nodes not connected by edge."""
#     graph.add_node('beer')
#     graph.add_node('wino')
#     assert graph.adjacent('beer', 'wino') is False


# def test_adjacent_reverse_is_false(graph):
#     """Test adjacent returns false for nodes connected by edge in opposite direction."""
#     graph.add_edge('beer', 'wine')
#     assert graph.adjacent('wine', 'beer') is False


# def test_add_duplicate_edge(graph):
#     """Test add_edge raises error if edge to add already exists on graph."""
#     graph.add_edge('rock', 'paper')
#     with pytest.raises(ValueError):
#         graph.add_edge('rock', 'paper')


# def test_nodes(graph):
#     """Test nodes returns list of all nodes in graph."""
#     graph.add_node('blah')
#     graph.add_node('whamo')
#     graph.add_node(2)
#     assert graph.nodes() == ['blah', 'whamo', 2]


# def test_nodes_no_nodes(graph):
#     """Test nodes returns list of all nodes in graph even if no nodes."""
#     assert graph.nodes() == []


# def test_edges(graph):
#     """Test edges returns list of all edges in graph."""
#     graph.add_edge('blah', 'whamo')
#     graph.add_edge('whamo', 'blah')
#     graph.add_edge(2, 'whamo')
#     assert str(graph.edges()) == "[('blah', 'whamo'), ('whamo', 'blah'), (2, 'whamo')]"


# def test_edges_no_edges(graph):
#     """Test edges returns list of all edges in graph even if no edges."""
#     assert graph.edges() == []


# def test_repr_edge(edge):
#     """Test __repr__ returns edge formatted as tuple."""
#     assert repr(edge) == "('node', 'another_node')"


# def test_neighbors_of_non_existing_node(graph):
#     """Test neighbors raises error when called for non-existent node."""
#     with pytest.raises(IndexError):
#         graph.neighbors('node')


def test_depth_complex(complex_g):
    assert complex_g == list('ABDXYEZ1CFG')