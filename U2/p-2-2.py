# sort + set + dict.__getitem__
def main():
    from sys import stdin
    e = stdin.readline

    e()
    l = tuple(map(int, e().split()))
    s = {v: i for i, v in enumerate(sorted(set(l)))}.__getitem__
    print(*map(s, l))
main()
