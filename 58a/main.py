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

s = 'hello'

t = I()
idx = 0
for i in s:
    while idx < len(t) and t[idx] != i:
        # print(t[idx])
        idx += 1

    if idx >= len(t):
        print("NO")
        break
    idx += 1
else:
    print("YES")