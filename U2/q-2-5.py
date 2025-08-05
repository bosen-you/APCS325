# 矩陣快速冪
def main():
    from sys import stdin
    e = stdin.readline

    def fab(n):
        if n < 3: return int(n>0)

        n -= 2
        d = p = (1, 1, 0)
        while n:
            if n & 1:
                p = matmul(p, d)
            d = matmul(d, d)
            n >>= 1
        return p[0]

    def matmul(a, b):
        x = (a[0] * b[0] + a[1] * b[1]) % p
        y = (a[0] * b[1] + a[1] * b[2]) % p
        z = (a[1] * b[1] + a[2] * b[2]) % p
        return (x, y, z)

    p = 1000000007
    it = map(int, stdin)
    n = next(it)
    for nxt in it:
        print(fab(n))
        n = nxt

main()
