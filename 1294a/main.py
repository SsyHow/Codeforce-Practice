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
    a, b,c,d = MII()
    summ = a + b + c + d
    if summ % 3:
        print("NO")
    else:
        ave = summ // 3
        if ave >= a and ave >= b and ave >= c:
            print("YES")
        else:
            print("NO")
