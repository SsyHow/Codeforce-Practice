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
s = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(a):
    b = I()
    if len(b) == 1:
        print(b, chr((ord(b) - ord('a') + 1) % 26 + ord('a')), sep='')
        continue
    prev = b[0]
    for i in range(1, len(b)):
        if b[i] == prev:
            print(b[:i], chr((ord(b[i]) - ord('a') + 1) % 26 + ord('a')), b[i:], sep='')
            break
        prev = b[i]
    else:
        print(b, chr((ord(b[-1]) - ord('a') + 1) % 26 + ord('a')),  sep='')
