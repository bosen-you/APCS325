# dict.__getitem__ + set + str.rstrip + ~i
def main():
    from sys import stdin
    e = stdin.readline

    get = {'A': 1, 'B': 2, 'C': 4, 'D': 8, 'E': 16, 'F': 32, 'G': 64,
           'H': 128, 'I': 256, 'J': 512, 'K': 1024, 'L': 2048, 'M': 4096,
           'N': 8192, 'O': 16384, 'P': 32768, 'Q': 65536, 'R': 131072,
           'S': 262144, 'T': 524288, 'U': 1048576, 'V': 2097152, 'W': 4194304,
           'X': 8388608, 'Y': 16777216, 'Z': 33554432}.__getitem__
    m, n = map(int, e().split())
    s = set()
    add = s.add

    for it in map(str.rstrip, stdin):
        bit = 0
        for i in map(get, it):
            bit |= i
        add(bit)

    everyone = (1 << m)-1
    print(sum(1 for i in s if (everyone & ~i) in s) >> 1)
main()
