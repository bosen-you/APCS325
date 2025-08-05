def main():
    from sys import stdin
    from bisect import bisect_left
    e = stdin.readline

    n, r = map(int, e().split())
    l = (0, *map(int, e().split()), r)

    ans = 0
    stk = []
    i, j = 0, n+1
    while True:
        ans += l[j] - l[i]
        if i + 2 == j:
            if stk:
                i, j = stk.pop()
                continue
            break

        mid = l[i]+l[j]
        idx = bisect_left(l, mid >> 1, lo = i+1, hi = j-1)
        if idx > i+1 and l[idx] + l[idx-1] >= mid:
            idx -= 1

        if i + 2 <= idx:
            if idx + 2 <= j:
                stk.append((idx, j))
            i, j = i, idx
        else:
            i, j = idx, j
    print(ans)
main()
