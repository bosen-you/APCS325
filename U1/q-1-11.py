# Prefix Sum + Exhaustive Algorithm
def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline

    m, n = map(int, e().split())
    area = m*n
    l = tuple(map(tuple, (map(int, e().split()) for _ in range(m))))

    pr = tuple((0, *accumulate(row)) for row in l)
    pc = tuple((0, *accumulate(col)) for col in zip(*l))

    dp = [[[[0]*j for j in range(n+1)] for _ in range(i)] for i in range(m+1)]

    for r in range(2, m+1): #row
        for s in range(m-r+1):
            t = s+r
            chuck = dp[t][s]
            for c in range(2, n+1): # col
                for i in range(n-c+1):
                    j = i+c
                    res = area

                    # up
                    x = pr[s][j] - pr[s][i]
                    x = min(x, c-x)
                    res = min(res, dp[t][s+1][j][i]+x)

                    #down
                    x = pr[t-1][j] - pr[t-1][i]
                    x = min(x, c-x)
                    res = min(res, dp[t-1][s][j][i]+x)

                    #left
                    x = pc[i][t] - pc[i][s]
                    x = min(x, r-x)
                    res = min(res, chuck[j][i+1]+x)

                    #right
                    x = pc[j-1][t] - pc[j-1][s]
                    x = min(x, r-x)
                    res = min(res, chuck[j-1][i]+x)

                    chuck[j][i] = res
    print(dp[m][0][n][0])
main()
