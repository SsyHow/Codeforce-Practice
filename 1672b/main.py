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
    s = I()
    x = y = 0
    if s[-1] == "A":
        print("NO")
        continue
    for i in s:
        if i == "A":
            x += 1
        else:
            y += 1
            if x < y:
                print("NO")
                break
    else:
        print("YES")


