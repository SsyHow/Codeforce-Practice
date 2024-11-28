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

n ,a, b, c = MII()
ans = 0
vis = []
for i in range(n//a+1):
    for j in range(n - i*a + 1):
        rem = n - i*a - j*b
        if rem % c == 0:
            k = rem // c
            if k >= 0:
                ans = max(i+j+k, ans)
                # vis.append((ans, i,j,k))
print(ans)
# print(vis)