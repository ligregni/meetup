# Clicks

class SegmentTree(object):
    def __init__(self, sizes):
        assert len(sizes) > 0
        assert min(sizes) > 0
        self.sze = len(sizes)
        self.build(sizes)

    def build(self, sizes):
        pass

    def size(self):
        return self.sze

    def update(self, index, size):
        assert index >= 0 and index < self.sze
        assert size > 0

class Clicker(object):
    ROW = 0
    COLUMN = 1

    def __init__(self, col_sizes, row_sizes):
        # Cannot be empty
        assert col_sizes and row_sizes

        self.cols = SegmentTree(col_sizes)
        self.rows = SegmentTree(row_sizes)

    def resize(self, typ, index, new_size):
        assert index >= 0 and index < (
            self.rows.size() if typ == Clicker.ROW else self.cols.size() )
        assert new_size > 0

    def click(self, x, y):
        assert x >= 0 and y >= 0
