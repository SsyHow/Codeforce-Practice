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
L = LII()
l, r = 0, a-1

if a == 1:
    print("yes")
    print(1, 1)

else:
    while l< r and L[l] < L[l+1]:
        l += 1
    while l < r and L[r] > L[r-1]:
        r -= 1

    M = L[:l] + L[l:r+1][::-1] + L[r+1:]
    # print(M, l, r)
    if M == sorted(L):
        print("yes")
        print(l+1, r+1)
    else:
        print('no')