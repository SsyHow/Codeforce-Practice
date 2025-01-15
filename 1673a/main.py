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
    b = I()
    n = len(b)

    L = [0] * n
    for i in range(n):
        L[i] = ord(b[i]) - ord('a') + 1

    if n & 1 == 0:
        print("Alice", sum(L))
    else:
        x, y = 0, 0
        alice = [sum(L[1:]), sum(L[:-1])]
        bob = [L[0], L[-1]]
        if (alice[0] - bob[0]) >= abs(alice[1] - bob[1]):
            x = alice[0]
            y = bob[0]
        else:
            x = alice[1]
            y = bob[1]

        if x > y:
            print("Alice", abs(x- y))
        else:
            print("Bob", abs(x - y))