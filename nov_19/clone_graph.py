from Queue import Queue
import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = list()

    def connect(self, other):
        self.neighbors.append(other)

def get_clone(node, mapa):
    if not node in mapa:
        mapa[node] = Node(node.val)
    return mapa[node]

def clone_graph(node):
    if not node:
        return None
    q = Queue()
    m = dict()
    q.put(node)
    cloned = get_clone(node, m)
    while not q.empty():
        n = q.get()
        for x in n.neighbors:
            if x not in m:
                q.put(x)
            get_clone(n, m).connect(get_clone(x, m))
    return cloned
