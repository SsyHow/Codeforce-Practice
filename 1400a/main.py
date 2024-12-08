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
    s = I()

    print('1' * b) if s.count('1') > s.count('0') else print("0" * b)

