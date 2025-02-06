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

def isprime(k):
    for i in range(2, k//2 + 1):
        if k % i == 0:
            return False
    return True

a = II()
for _ in range(a):
    b = II()
    L = LII()
    c = sum(L)
    if isprime(c):
        print(b-1)
        for i in L:
            if i % 2 == 1:
                break

        for idx, k in enumerate(L):
            if k == i:
                continue
            print(idx + 1, end = ' ')
        print()

    else:
        print(b)
        print(*range(1, b+1))
