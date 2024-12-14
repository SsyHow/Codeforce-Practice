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

n, b, d = MII()
L = LII()
was = 0
cnt = 0
for i in L:
    if i > b:
        continue
    was += i

    if was > d:
        cnt += 1
        was = 0
print(cnt)