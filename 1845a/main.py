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
    n, k, x = MII()
    if x != 1:
        print("YES")
        print(n)
        print('1 ' * n)

    elif k == 1:
        print("NO")
    elif k == 2:
        if n % 2 == 1:
            print("NO")
        else:
            print("YES")
            print(n // 2)
            print('2 ' * (n//2))
    else:
        print("YES")
        print(n//2)
        print('2 ' * (n // 2 - 1)  + '3') if n % 2 == 1 else print('2 ' * (n//2))