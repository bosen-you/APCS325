# meet-in-the-middle (MITM)
def main():
    from sys import stdin, stdout
    from itertools import islice
    from bisect import bisect_left
    e = stdin.readline

    n, p = map(int, e().split())
    l = map(int, e().split())
    x = next(l) 
  
    sa, sb = [0], [0]
    for i in islice(l, n>>1):
        for v in islice(sa, len(sa)):
            v += i
            if v < p: sa.append(v)

    for i in l:
        for v in islice(sb, len(sb)):
            v += i
            if v < p: sb.append(v)

    sb.sort()
    mx = sb[-1]
    ans = 0

    for i in sa:
        if ans - mx < i:
            idx = bisect_left(sb, p-i)-1
            ans = max(ans, i+sb[idx])
        i += x
        if ans - mx < i <= p:
            idx = bisect_left(sb, p-i)-1
            ans = max(ans, i+sb[idx])
    stdout.write(str(ans)) 
main()
