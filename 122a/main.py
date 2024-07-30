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

a = I()
b = set(a)
if b.issubset({'4', '7'}):
    print("YES")
else:
    for i in range(1, int(a) // 2+ 1):
        if int(a) % i == 0  and set(str(i)).issubset({'4', '7'}):
            print("YES")
            break
    else:
        print("NO")