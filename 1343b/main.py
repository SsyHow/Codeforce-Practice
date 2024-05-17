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
    if b %4 :
        print("NO")
    else:
        print("YES")
        L = [str(i) for i in range(2, b+1, 2)]
        M = [str(i) for i in range(1, b, 2)]
        M[-1] = str(int(M[-1])+len(L))
        L.extend(M)
        print(' '.join(L))
