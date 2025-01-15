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

    for i in range(ord('a'), ord('z') + 1):
        c = s.rfind(chr(i))
        if c != -1:
            print(s[c] + s[:c] + s[c+1:])
            break
