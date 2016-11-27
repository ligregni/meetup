# Knight problem

import sys
from Queue import Queue

deltas = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

def is_valid(pos):
    if pos[0] >= 0 and pos[0] < 8 and pos[1] >=0 and pos[1] < 8:
        return True
    return False

def moves(start):
    m = list()
    for x in deltas:
        n = (start[0]+x[0], start[1]+x[1])
        if is_valid(n):
            m.append(n)
    return m

def bfs(start, end):
    q = Queue()
    m = set()
    q.put((start, 0))
    while not q.empty():
        pos = q.get()
        if pos[0] in m:
            continue
        m.add(pos[0])
        if pos[0] == end:
            return pos[1]
        for x in moves(pos[0]):
            q.put((x, pos[1]+1))
    return -1

if __name__ == '__main__':
    start = tuple([ int(x) for x in sys.argv[1:3]])
    end = tuple([ int(x) for x in sys.argv[3:5]])
    print bfs(start, end)
