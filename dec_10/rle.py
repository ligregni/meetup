# RLE

def add_elem(s, elem, count, index):
    if count <= 2:
        for i in xrange(count):
            s[index] = elem
            index += 1
        return index

    for x in str(count):
        s[index] = x
        index += 1
    s[index] = elem
    return index + 1

def encode(s):
    count = 0
    elem = None
    index = 0
    for x in s:
        if x != elem:
            index = add_elem(s, elem, count, index)
            count = 1
            elem = x
        else:
            count += 1
    index = add_elem(s, elem, count, index)
    if index == len(s):
        s.append(None)
    else:
        s[index] = None
