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
    n, k = MII()
    L = LII()
    c = {1, 7, 17, 119, 289, 2023}
    p = 1
    for i in L:
        p *= i
        if i not in c or 2023 % p != 0:
            print("NO")
            break
    else:
        print(f'YES\n{2023 // p}', '1 '* (k-1))




