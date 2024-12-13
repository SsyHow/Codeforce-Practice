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
    odd = []
    even = []
    for i in MII():
        if i % 2 == 1:
            odd.append(str(i))
        else:
            even.append(str(i))
    print(' '.join(odd), end = ' ')
    print(' '.join(even))
