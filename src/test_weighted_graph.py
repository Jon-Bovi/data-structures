"""Testing module for Graph class."""
import pytest


@pytest.fixture
def graph():
    """Return initialized graph."""
    from weighted_graph import Graph
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


def test_add_node_with_ordered_dict(graph):
    """Test add_node adds node to graph."""
    graph.add_node('node')
    assert graph.has_node('node')


def test_add_edge(complex_g):
    """Test that add_edge adds edge with source and dest."""
    assert len(complex_g.edges()) > 0


def test_add_edge_error(complex_g):
    """Test del_edge raises error if adds an edge that already exists."""
    with pytest.raises(ValueError):
        complex_g.add_edge('C', 'G')


def test_del_node_error(complex_g):
    """Test del_node raises error if node to be deleted doesn't exist."""
    complex_g.add_node('mama')
    with pytest.raises(KeyError):
        complex_g.del_node('dada')


def test_delete_edge_error(complex_g):
    """Test del_edge raises error if edge to be deleted doesn't exist."""
    complex_g.add_edge('node', 'edon')
    with pytest.raises(KeyError):
        complex_g.del_edge('node', 'noooode')


def test_del_node(complex_g):
    """Test del_node removes node."""
    complex_g.add_node('node')
    complex_g.del_node('node')
    assert 'node' not in complex_g.node_dict


def test_del_edge(graph):
    """Test del edge removes edge."""
    graph.add_edge('node', 'edon', 2)
    graph.del_edge('node', 'edon')
    assert len(graph.edges()) == 0


def test_del_edge_error(graph):
    """Test del_edge raises error if edge to be deleted doesn't exist."""
    graph.add_edge('node', 'edon')
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
    graph.add_edge('car', 'bank', 2)
    graph.add_edge('car', 'wheels', 3)
    assert graph.neighbors('car') == ['bank', 'wheels']


def test_neighbors_error(graph):
    """Test neighbors returns all nodes connected to a single node."""
    graph.add_edge('car', 'bank')
    graph.add_edge('car', 'wheels')
    with pytest.raises(KeyError):
        graph.neighbors('house') == ['bank', 'wheels']


def test_adjacent_true(graph):
    """Test adjacent returns true for nodes connected by edge."""
    graph.add_edge('beer', 'wine')
    assert graph.adjacent('beer', 'wine')


def test_adjacent_false(graph):
    """Test adjacent returns false for nodes not connected by edge."""
    graph.add_node('beer')
    graph.add_node('wino')
    assert graph.adjacent('beer', 'wino') is False


def test_adjacent_reverse_is_false(graph):
    """Test adjacent returns false for nodes connected by edge in opposite direction."""
    graph.add_edge('beer', 'wine')
    with pytest.raises(KeyError):
        graph.adjacent('wine', 'sake')


def test_add_duplicate_edge(graph):
    """Test add_edge raises error if edge to add already exists on graph."""
    graph.add_edge('rock', 'paper', 5)
    with pytest.raises(ValueError):
        graph.add_edge('rock', 'paper', 5)


def test_nodes(graph):
    """Test nodes returns list of all nodes in graph."""
    graph.add_node('blah')
    graph.add_node('whamo')
    graph.add_node(2)
    assert 'blah' in (graph.nodes())
    assert 'whamo' in (graph.nodes())
    assert 2 in (graph.nodes())


def test_nodes_no_nodes(graph):
    """Test nodes returns list of all nodes in graph even if no nodes."""
    assert graph.nodes() == []


def test_edges(graph):
    """Test edges returns list of all edges in graph."""
    graph.add_edge('blah', 'whamo', 5)
    graph.add_edge('whamo', 'blah', 6)
    graph.add_edge('snarky', 'whamo', 7)
    assert ('blah', 'whamo', 'weight: 5') in list((graph.edges()))
    assert ('whamo', 'blah', 'weight: 6') in list((graph.edges()))
    assert ('snarky', 'whamo', 'weight: 7') in list((graph.edges()))


def test_edges_no_edges(graph):
    """Test edges returns list of all edges in graph even if no edges."""
    assert graph.edges() == []


def test_neighbors_of_non_existing_node(graph):
    """Test neighbors raises error when called for non-existent node."""
    with pytest.raises(KeyError):
        graph.neighbors('node')


def test_depth_complex(complex_g):
    """Test the depth traversal graph."""
    g = complex_g
    res = g.depth_first_traversal('A')
    assert res == list('ABDXYEZCFG')


# def test_depth_complex_iterative(complex_g):
#     """Test the depth traversal graph."""
#     g = complex_g
#     res = g.depth_first_traversal_iterative('A')
#     assert res == list('ABDXYEZCFG')


def test_breadth_complex(complex_g):
    """Test the breadth traversal graph."""
    g = complex_g
    res = g.breadth_first_traversal('A')
    assert res == list('ABCDEFGXYZ')


def test_add_edge_depth(complex_g):
    """Test traversal after adding edge."""
    g = complex_g
    g.add_edge('B', 'C')
    res = g.breadth_first_traversal('A')
    assert res == list('ABCDEFGXYZ')
