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
def solve():
    b = II()
    for i in range(1, 3):
        for j in range(2, 6):
            if i + j >= b or i == j or j % 3 == 0:
                continue
            k = b - i - j
            if k == i or k == j or k % 3 == 0:
                continue
            print("YES")
            print(i, j, k)
            return
    else:
        print("NO")
        return
for _ in range(a):
    solve()