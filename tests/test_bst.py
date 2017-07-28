"""Test binary search tree implementation."""

import pytest


@pytest.fixture
def test_bsts():
    """Fixture for bst."""
    from src.bst import Bst
    empty = Bst()
    one = Bst([5])
    three = Bst([5, 3, 7])
    balance = Bst([5, 3, 2, 4, 9, 7, 10])
    leftheavy = Bst([5, 3, 2, 1])
    rightheavy = Bst([5, 6, 7, 8, 9, 10])
    return empty, one, three, balance, leftheavy, rightheavy


@pytest.fixture
def test_traversals():
    """Fixture for traversals."""
    from src.bst import Bst
    fixture = {
        'tree': Bst(['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']),
        'pre_order': ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H'],
        'in_order': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'post_order': ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F'],
        'breadth': ['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H']
    }
    return fixture


def test_node_is_leaf(test_bsts):
    """Test node is leaf bst."""
    assert test_bsts[1].root.is_leaf()


def test_insert_sets_root(test_bsts):
    """Test first insert updates root."""
    test_bsts[0].insert(5)
    assert test_bsts[0].root.val == 5


def test_insert_updates_pointers(test_bsts):
    """Test insert updates pointers."""
    test_bsts[1].insert(3)
    assert test_bsts[1].root.left.val == 3
    assert test_bsts[1].root.left.parent == test_bsts[1].root


def test_insert_smallest_left(test_bsts):
    """Test insert the smallest to the left."""
    test_bsts[1].insert(3)
    assert test_bsts[1].root.left.val < test_bsts[1].root.val


def test_insert_largest_right(test_bsts):
    """Test insert the largest to the right."""
    test_bsts[1].insert(7)
    assert test_bsts[1].root.right.val > test_bsts[1].root.val


def test_insert_increases_size(test_bsts):
    """Test insert increases size."""
    test_bsts[0].insert(4)
    assert test_bsts[0].size() == 1


def test_contains_method(test_bsts):
    """Test contains on number that exists."""
    assert test_bsts[2].contains(5)
    assert test_bsts[2].contains(3)
    assert test_bsts[2].contains(7)


def test_contains_method_no_val(test_bsts):
    """Test contains that doesnt exist."""
    assert not test_bsts[4].contains(10)


def test_depth_method(test_bsts):
    """Test depth method."""
    depths = [0, 1, 2, 3, 4, 6]
    assert all(tree.depth() == depths[idx]
               for idx, tree in enumerate(test_bsts))


def test_balance_method(test_bsts):
    """Test the balance method."""
    balance = [0, 0, 0, 0, 3, -5]
    assert all(tree.balance() == balance[idx]
               for idx, tree in enumerate(test_bsts))


def test_search_method_node_exists(test_bsts):
    """Test search method for a node that exists."""
    assert all(tree.search(5) for tree in test_bsts[1:])


def test_pre_order(test_traversals):
    """Test preorder for a traversal."""
    path = [i for i in test_traversals['tree'].pre_order()]
    assert path == test_traversals['pre_order']


def test_in_order(test_traversals):
    """Test inorder for a traversal."""
    path = [i for i in test_traversals['tree'].in_order()]
    assert path == test_traversals['in_order']


def test_post_order(test_traversals):
    """Test postorder for a traversal."""
    path = [i for i in test_traversals['tree'].post_order()]
    assert path == test_traversals['post_order']


def test_breadth_first(test_traversals):
    """Test breadth first for a traversal."""
    path = [i for i in test_traversals['tree'].breadth_first()]
    assert path == test_traversals['breadth']
