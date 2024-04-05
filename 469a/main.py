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
b = set(LII()[1:])
c = set(LII()[1:])

d = set(range(1, a+1))
c = c|b
print('Oh, my keyboard!' if d-c != set() else 'I become the guy.')