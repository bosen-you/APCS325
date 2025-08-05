def main():
    from sys import stdin
    e = stdin.readline

    x, y, p = map(int, e().split())

    t = 1; xi = x
    while y > 0:
        if y & 1:
            t = t*xi%p
        y >>= 1
        xi = xi*xi%p

    print(t)
main()
