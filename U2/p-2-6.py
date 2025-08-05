# set
def main():
    from sys import stdin
    e = stdin.readline

    m, n, k = map(int, e().split())
    a = set(map(int, e().split()))
    print(sum(1 for i in map(int, e().split() if k-i in a))
main()
