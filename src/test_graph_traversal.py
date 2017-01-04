"""Testing module for Stack class."""
import pytest


@pytest.fixture
def graph():
    """Return initialized graph."""
    from graph_traversal import Graph
    return Graph()


@pytest.fixture
def complex_g(graph):
    """."""
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
    assert 'node' in graph.nodes()


def test_add_edge(complex_g):
    """Test that add_edge adds edge with source and dest."""
    assert len(complex_g.edges()) > 0


def test_add_edge_error(complex_g):
    """Test del_edge raises error if adds an edge that already exists."""
    with pytest.raises(ValueError):
        complex_g.add_edge('C', 'G')


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


def test_del_node_error(complex_g):
    """Test del_node raises error if node to be deleted doesn't exist."""
    complex_g.add_node('mama')
    with pytest.raises(KeyError):
        complex_g.del_node('dada')


def test_del_edge(graph):
    """Test del edge removes edge."""
    graph.add_edge('node', 'edon')
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
    graph.add_edge('car', 'bank')
    graph.add_edge('car', 'wheels')
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
    graph.add_edge('rock', 'paper')
    with pytest.raises(ValueError):
        graph.add_edge('rock', 'paper')


def test_nodes(graph):
    """Test nodes returns list of all nodes in graph."""
    graph.add_node('blah')
    graph.add_node('whamo')
    graph.add_node('zeno')
    assert sorted(graph.nodes()) == ['blah', 'whamo', 'zeno']


def test_nodes_no_nodes(graph):
    """Test nodes returns list of all nodes in graph even if no nodes."""
    assert graph.nodes() == []


def test_edges(graph):
    """Test edges returns list of all edges in graph."""
    graph.add_edge('blah', 'whamo')
    graph.add_edge('whamo', 'blah')
    graph.add_edge(2, 'whamo')
    assert ('blah', 'whamo') in graph.edges()
    assert ('whamo', 'blah') in graph.edges()
    assert (2, 'whamo') in graph.edges()


def test_edges_no_edges(graph):
    """Test edges returns list of all edges in graph even if no edges."""
    assert graph.edges() == []


def test_neighbors_of_non_existing_node(graph):
    """Test neighbors raises error when called for non-existent node."""
    with pytest.raises(KeyError):
        graph.neighbors('node')


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
    assert res == list('ABDXYEZ1CFG')


def test_depth_iterative_complex(complex_g):
    """Test the depth traversal graph."""
    res = complex_g.depth_first_traversal_iterative('A')
    assert res == list('ABDXYEZ1CFG')


def test_breadth_complex(complex_g):
    """Test the breadth traversal graph."""
    res = complex_g.breadth_first_traversal('A')
    assert res == list('ABCDEFGXYZ1')


def test_add_edge_depth(complex_g):
    """Test traversal after adding edge."""
    g = complex_g
    g.add_edge('B', 'C')
    res = g.breadth_first_traversal('A')
    assert res == list('ABCDEFGXYZ1')
