def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))


p1 = 1
p2 = 1
ans = [1, 1]
for i in range(14):
    pk = p1 + p2
    ans.append(pk)
    p1 = p2
    p2 = pk

c = ['o'] * 1000

for i in ans:
    c[i-1] = 'O'
a = II()
print(''.join(c)[:a])