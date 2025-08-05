# Modular multiplicative inverse
def main():
    from sys import stdin
    e = stdin.readline

    n, p = map(int, e().split())
    # python > 3.8
    print(*(pow(i, -1, p) for i in map(int, e().split())))
    # python < 3.8 
    # print(*(pow(i, p-2, p) for i in map(int, e().split())))
main()
