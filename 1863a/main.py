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
    x, y, z = MII()
    s = I()
    if x == y:
        print("YES")
        continue

    a = s.count('+')
    b = s.count('-')

    if y + a < x:
        print("NO")
        continue
    k = y
    for i in s:
        if i == '+':
            k += 1
        else:
            k -= 1
        if k == x:
            print("YES")
            break
    else:
        print("MAYBE")