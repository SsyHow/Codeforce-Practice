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
    L = sorted(input().split(), key=lambda x: len(x))

    for i in range(0, 2*b - 2, 2):

        if sorted(L[i]) != sorted(L[i+1]):
            print("NO")
            break
    else:
        print("YES")


