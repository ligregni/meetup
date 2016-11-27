from collections import defaultdict
import logging
import unittest

from clone_graph import *

def build_edge(a, b):
    return (a.val, b.val)
    # return (min(a.val, b.val), max(a.val, b.val))

def build_edges_list(node, nodes, edges):
    if not node:
        return
    nodes.add(node.val)
    for n in node.neighbors:
        edges[build_edge(node, n)] += 1
        if n.val not in nodes:
            build_edges_list(n, nodes, edges)

def build_graph(node):
    nodes = set()
    edges = defaultdict(int)
    build_edges_list(node, nodes, edges)
    return nodes, edges

class CloneGraph(unittest.TestCase):
    def setUp(self):
        pass

    def assert_cloned_graph_equal(self, original):
        clone = clone_graph(original)
        n1,e1 = build_graph(original)
        n2,e2 = build_graph(clone)
        self.assertEqual(n1, n2)
        self.assertEqual(e1, e2)

    def test_empty_graph(self):
        self.assert_cloned_graph_equal(None)

    def test_single_node_graph(self):
        self.assert_cloned_graph_equal(Node(6))

    def test_single_list(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        a.connect(b)
        b.connect(c)
        c.connect(d)
        self.assert_cloned_graph_equal(a)

    def test_double_linked_list(self):
        a = Node(6)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        a.connect(b)
        b.connect(a)
        b.connect(c)
        c.connect(b)
        c.connect(d)
        d.connect(c)
        self.assert_cloned_graph_equal(a)

    def test_circular_list(self):
        a = Node(1)
        b = Node(2)
        a.connect(b)
        b.connect(a)
        self.assert_cloned_graph_equal(a)

    def test_tree(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        a.connect(b)
        a.connect(c)
        c.connect(d)
        self.assert_cloned_graph_equal(a)

    def test_graph_no_cycles(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        a.connect(b)
        a.connect(c)
        b.connect(d)
        c.connect(d)
        self.assert_cloned_graph_equal(a)

    def test_graph_with_cycles(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        a.connect(b)
        b.connect(c)
        c.connect(d)
        c.connect(a)
        self.assert_cloned_graph_equal(a)
