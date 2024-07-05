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
    b = II()
    x = I()
    y = I()
    for j in range(b):
        if "R" in (x[j], y[j]) and "B" in (x[j], y[j]):
            print("NO")
            break
        elif "R" in (x[j], y[j]) and "G" in (x[j], y[j]):
            print("NO")
            break
    else:
        print("YES")