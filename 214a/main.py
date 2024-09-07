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

def main():
    n, m = MII()
    cnt = 0
    for i in range(n+1):
        for j in range(m+1):

            if i ** 2 + j == n and j ** 2 + i == m:
                cnt += 1
            if i ** 2 + j > n and j ** 2 + i > m:
                break

    print(cnt)
main()
