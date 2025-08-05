# meet-in-the-middle (MITM) + defaultdict + modular multiplicative inverse
def main():
    from sys import stdin
    from itertools import islice
    from collections import defaultdict
    e = stdin.readline
    p = 10009

    n = int(e())
    l = map(int, e().split())

    # MITM
    sa, sb = defaultdict(int), defaultdict(int)
    sa[1] = sb[1] = 1
    for i in islice(l, n >> 1):
        for k, v in tuple(sa.items()):
            sa[k * i % p] += v
    for i in l: 
        for k, v in tuple(sb.items()):
            sb[k * i % p] += v
    ''' 
    m ε sa, k ε sb
    because m * k Ξ 1 mod p
    => m Ξ k^(-1) mod p 
    therefore m Ξ k^(p-2) mod p ( k^(-1) = k^(p-2) )

    sum -1 => 扣掉sa[0]*sb[0] (sa[0] = sb[0] = 1
    ''' 
    print(sum(v*sb[pow(k, k-2, p)] for k, v in sa.items()) -1) 
main()
