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
    n = II()
    i = 2
    j = 0
    ans = []
    while j < 2 and i * i < n:
        if n % i == 0:
            ans.append(str(i))
            n //= i
            j += 1
        i += 1
    # print(j)
    if j == 2:

        print(f"YES")
        print(*ans, n, sep=' ')
    else:
        print("NO")



