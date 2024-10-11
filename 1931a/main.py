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
for i in range(a):
    x,y,z = 1,1,1
    b = II() - 3
    z += min(b, 25)
    y += max(0, min(b-25, 25))
    x += max(0, min(b-50, 25))
    print(chr(ord('a')-1 + x), chr(ord('a')-1 + y), chr(ord('a')-1 + z), sep='')
