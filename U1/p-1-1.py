def cal(l):
    token = l.pop()
    return 2*cal(l)-1 if token == 'f' else cal(l)+2*cal(l)-3 if token == 'g' else int(token)

print(cal([str(i) for i in input().split()][::-1]))
