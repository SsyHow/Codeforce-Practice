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
    s = I()
    if s[-2:] == 'po':
        print("FILIPINO")
    elif s[-2:] == 'su':
        print("JAPANESE")
    else:
        print("KOREAN")