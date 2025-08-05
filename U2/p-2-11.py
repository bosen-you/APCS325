# itertools.accumualte + bisect.bisect_left(<x) + bisect.insort(黑魔法) 
def main():
    from sys import stdin
    from itertools import accumulate
    from bisect import bisect_left, insort
    e = stdin.readline

    n, k = map(int, e().split())

    s = [0]; ans = 0
    for v in accumulate(map(int, e().split())):
        if v-s[-1] <= k:
            idx = bisect_left(s, v-k)
            ans = max(ans, v - s[idx])
        insort(s, v)
    print(ans)
main()
