def cal(l):
    token = l.pop()
    return 2*cal(l)-3 if token == 'f' else 2*cal(l)+cal(l)-7 if token == 'g' else 3*cal(l)-2*cal(l)+cal(l) if token == 'h' else int(token) 

print(cal([str(i) for i in input().split()][::-1]))
