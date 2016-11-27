# Character Swap

from collections import defaultdict

class DisjointSet(object):
    '''
    Cheap (non-optimized) disjoint set implementation.
    '''
    def __init__(self, n):
        self.sets = range(n)

    def find(self, a):
        if self.sets[a] != a:
            self.sets[a] = self.find(self.sets[a])
        return self.sets[a]

    def union(self, a, b):
        self.sets[self.find(a)] = self.find(b)

    def get_sets(self):
        h = defaultdict(set)
        for elem in range(len(self.sets)):
            h[self.find(elem)].add(elem)
        return h

def optimize_group(s, indexes):
    tmp = list()
    for index in indexes:
        tmp.append(s[index])

    tmp.sort(reverse=True)
    sorted_indexes = sorted(list(indexes))
    for index in sorted_indexes:
        s[index] = tmp.pop(0)

def longest_swap(s, indexes):
    if len(indexes) == 0:
        return s

    sets = DisjointSet(len(s))
    for a,b in indexes:
        sets.union(a, b)

    groups = sets.get_sets()
    string = list(s)
    for key,group in groups.iteritems():
        optimize_group(string, group)

    return ''.join(string)
