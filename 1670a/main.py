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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
for _ in range(a):
    b = II()
    L = LII()
    # M = sorted(L)
    neg = sum(1 for i in L if i < 0)

    L = [abs(i) for i in L]
    i = 0
    # print(L, neg)
    while neg > 0 :
        L[i] = -L[i]
        neg  -= 1
        i+= 1
    # print(L, neg)
    for i in range(b-1):

        if L[i+1] < L[i]:
            print("NO")
            break
    else:
        print("YES")

