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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

x, y, z = MII()

if (x - y - z) > 0:
    print("+")
elif (x - y + z) < 0:
    print('-')

elif (x - y - z) == (x - y + z) == 0:
    print("0")
else:
    print("?")