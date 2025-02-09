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

a, b = MII()
i = 1

while True:

    if i & 1 == 1:
        a -= i
        if a < 0 :
            print("Vladik")
            break
    else:
        b -= i
        if b < 0 :
            print("Valera")
            break

    i += 1

