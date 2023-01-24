def f(l, m, s):
    for i in range(l):
        for j in range(i+1,l):
            if (m[i] + m[j])==s:
                return (m[i], m[j])
    return (None,)

l = int(input())
m = list(map(int,input().split()))
s = int(input())

print(*f(l,m,s))