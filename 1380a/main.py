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
    L = LII()

    for i in range(1, b-1):
        if L[i-1] < L[i] and L[i] > L[i+1]:
            print("YES")
            print(i, i+1, i+2)
            break
    else:
        print("NO")