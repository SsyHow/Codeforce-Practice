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

a = II()
s = I().split('W')
L = []
for i in s:
    if i != '' :
        L.append(len(i))

print(len(L))
print(*L)

