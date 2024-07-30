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

a = I().lower()
ans = ''

for i in a:
    if i in 'aeiouy':
        continue
    ans += '.' + i
print(ans)