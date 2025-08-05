'''
monotomic stack
itertools.accumulate + bisect.bisect_left(<x or >= x) 
'''
def main():
    from sys import stdin
    from itertools import accumulate
    from bisect import bisect_left
    e = stdin.readline

    n, m = map(int, e().split())
    l = (0, *(accumulate(map(int, e().split()))))

    idx = 0; last = l[-1]
    for v in map(int, e().split()):
        rest = last - l[idx]
        if rest == v:
            idx = 0
        else:
            if rest < v:
                v -= rest
                idx = 0
            idx = bisect_left(l, l[idx]+v)
    print(0 if idx == n else idx)
main()
