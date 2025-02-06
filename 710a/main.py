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

side = 0

s =I()
if s[0] == 'a' or s[0] == 'h':
    side += 1
if s[1] == '1' or s[1] == '8':
    side += 1

if side == 0:
    print(8)
elif side == 1:
    print(5)
else:
    print(3)