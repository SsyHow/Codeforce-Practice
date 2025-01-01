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

    l = 0
    r = len(b) - 1

    while l <= r:
        if b[l] != 'a':
            print("YES")
            print(b[:r+1] + 'a' + b[r+1:])
            break
        elif b[r] != 'a':
            print("YES")
            print(b[:l] + 'a' + b[l:])
            break
        l += 1
        r -= 1
    else:
        print("NO")