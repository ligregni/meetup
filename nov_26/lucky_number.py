def get_sum(x):
    return sum([int(x) in str(x)])

def lucky_number(n):
    while get_sum(n) < 10:
        n = get_sum(n)
    return n

if __name__ == '__main__':
    lucky_number(sys.argv[1])
