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

    for i in range(b-1):
        if s[i:i+2] == 'ab' or s[i:i+2] == 'ba':
            print(i+1, i+2)
            break
    else:
        print(-1, -1)