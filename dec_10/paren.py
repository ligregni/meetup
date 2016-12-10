memo = dict()

# Wrong!!!
def solve(n):
    if n == 0:
        return set()
    if n == 1:
        return set(['()'])
    if n in memo:
        return memo[n]

    sub = solve(n - 1)
    ret = set()
    for x in sub:
        tmp = '(' + x + ')'
        if tmp not in ret:
            ret.add(tmp)
        tmp = '()' + x
        if tmp not in ret:
            ret.add(tmp)
        tmp = x + '()'
        if tmp not in ret:
            ret.add(tmp)
    memo[n] = ret
    return memo[n]


# Correct
def solve2_inner(n, opened, s, result):
    if n == 0 and opened == 0:
        result.add(s)
        return

    if n > 0:
        solve2_inner(n-1, opened+1, s+'(', result)
    if opened > 0:
        solve2_inner(n, opened-1, s+')', result)

def solve2(n):
    if n == 0:
        return set()
    result = set()
    solve2_inner(n, 0, '', result)
    return result
