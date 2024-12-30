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
for _ in range(a):
    b = II()
    s = set()
    for i in MII():
        if i - 1 in s or i + 1 in s:
            print(2)
            break
        s.add(i)
    else:
        print(1)
