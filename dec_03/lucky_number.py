import sys

def get_sum(x):
    return sum([int(z) for z in str(x)])

def lucky_number(n):
    while get_sum(n) >= 10:
        n = get_sum(n)
    return get_sum(n)

if __name__ == '__main__':
    print lucky_number(int(sys.argv[1]))
