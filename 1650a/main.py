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
    b = I()
    c = I()
    for i in range(0, len(b), 2):
        if b[i] == c:
            print("YES")
            break
    else:
        print("NO")