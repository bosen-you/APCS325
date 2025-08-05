# irrational number + quick power
def main():
    from sys import stdin
    e = stdin.readline
    p = 1000000009

    i, j, n = map(int, e().split())
    n -= 1
    x, y = i, j
    while n > 0:
        if n & 1 == 1:
            i, j= (i*x + 2*j*y)%p, (x*j + y*i)%p
        x, y = (x*x + 2*y*y)%p, (2*x*y)%p
        n >>= 1
    print(i, j)
main()
