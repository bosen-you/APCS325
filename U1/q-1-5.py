area, flag = 0, 0
def cut(l):
    global area, flag
    for _ in range(4):
        if flag == len(s): return
        if s[flag] == '2':
            flag += 1
            cut(l//2)
        elif s[flag] == '1':
            flag += 1
            area += l*l
        else:
            flag += 1

s = input()
n = int(input())

cut(n)
print(area)
