# sort + set
def main():
    from sys import stdin
    e = stdin.readline

    e()
    l = sorted(set(map(int, e().split())))

    print(len(l))
    print(*l)
main()
