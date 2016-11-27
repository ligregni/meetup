# Oranges

from Queue import Queue
import sys

deltas = [(0,1), (0,-1), (-1,0), (1,0)]
EMPTY = 0
FRESH = 1
STALE = 2

matrixA = \
[[ EMPTY, EMPTY, FRESH, EMPTY ],
 [ FRESH, STALE, STALE, FRESH ],
 [ EMPTY, EMPTY, FRESH, EMPTY ],
 [ FRESH, STALE, FRESH, EMPTY ]]

matrixB = \
[[ EMPTY, EMPTY, FRESH, EMPTY ],
 [ FRESH, STALE, STALE, FRESH ],
 [ EMPTY, EMPTY, FRESH, EMPTY ],
 [ FRESH, STALE, FRESH, EMPTY ],
 [ EMPTY, EMPTY, EMPTY, FRESH ]]

matrix = [matrixA, matrixB]

def is_valid(pos, m, n):
    return pos[0] >= 0 and pos[0] < m and pos[1] >= 0 and pos[1] < n

def moves(pos, m, n):
    r = list()
    for x in deltas:
        p = (pos[0]+x[0], pos[1]+x[1])
        if is_valid(p, m, n):
            r.append(p)
    return r

def count_fresh(matrix):
    r = 0
    for row in matrix:
        for elem in row:
            if elem == FRESH:
                r += 1
    return r

def flood(matrix, start):
    fresh = count_fresh(matrix)
    if fresh == 0:
        return 0
    if matrix[start[0]][start[1]] != STALE:
        return -1
    m = len(matrix)
    n = len(matrix[0])
    q = Queue()
    visited = set()
    q.put((start, 0, fresh))
    while not q.empty():
        cell,days,left = q.get()
        if cell in visited:
            continue
        if left == 0:
            return days
        visited.add(cell)
        for dst in moves(cell, m, n):
            orange = matrix[dst[0]][dst[1]]
            if orange != EMPTY:
                if orange == FRESH:
                    fresh -= 1
                matrix[dst[0]][dst[1]] = STALE
                q.put(((dst[0], dst[1]), days+1, fresh))
    return -1

if __name__ == '__main__':
    matrix_to_use = int(sys.argv[1])
    start = tuple([ int(x) for x in sys.argv[2:4] ])
    print flood(matrix[matrix_to_use], start)
