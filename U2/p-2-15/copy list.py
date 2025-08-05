'''
copy the list
itertools.accumulate + bisect.bisect_left(<x or >= x) 
'''
def main():
    from sys import stdin
    from bisect import bisect_left
    from itertools import accumulate
    e = stdin.readline

    n, m = map(int, e().split())
    l = list(map(int, e().split()))
    p = (0, *accumulate(l + l.copy()))

    last = p[-1]; idx = 0
    for v in map(int, e().split()):
        rest = last - p[idx]
        if rest == v:
            idx = 0
        else:
            if rest < v:
                v -= rest
                idx = 0
            idx = bisect_left(p, p[idx]+v)
    print(idx % n)
main()
