
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

if a % 4 == 1:
    print(0, 'A')
elif a % 4 == 2:
    print(1, 'B')
elif a % 4 == 3:
    print(2, 'A')
else:
    print(1, 'A')