def cut(left, right, l, r):
    if l >= r: return 0

    mid = (left+right) / 2
    best = -1
    best_dist = float('inf')

    for i in range(l, r):
        d = abs(arr[i] - mid)
        if d < best_dist or (d == best_dist and best != -1 and arr[i] < arr[best]):
            best = i
            best_dist = d

    if best == -1: return 0

    cut_pos = arr[best]
    return right-left + cut(left, cut_pos, l, best) + cut(cut_pos, right, best+1, r)

n, m = map(int, input().split())
arr = [int(i) for i in input().split()]
print(cut(0, m, 0, n))
