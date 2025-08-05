def main():
    from sys import stdin
    from itertools import accumulate, starmap
    e = stdin.readline

    n, k = map(int, e().split())
    l = tuple(map(int, e().split()))

    p = (0, *accumulate(l))
    xp = (0, *accumulate(starmap(int.__mul__, enumerate(l))))

    ans = 0
    stk = [(0, n, 1)]
    append, pop = stk.append, stk.pop

    while stk:
        i, j, t = pop()

        sxp, sp = xp[j]-xp[i], p[j]-p[i]
        q, r = divmod(sxp, sp)
        if r > sp>>1:
            q += 1

        if q <= i:
            q = i+1
        elif q >= j-1:
            q = j-2

        ans += l[q]

        if t < k:
            d = q-i
            if d == 3:
                ans += l[i+1]
            elif d > 3:
                append((i, q, t+1))

            d = j - q - 1
            if d == 3:
                ans += l[q+2]
            if d > 3:
                append((q+1, j, t+1))
    print(ans)
main()
