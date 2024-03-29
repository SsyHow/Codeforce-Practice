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
b = I()
A = b.count('A')
D = b.count('D')
if A > D:
    print('Anton')
elif A < D:
    print('Danik')
else:
    print('Friendship')