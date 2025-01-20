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


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

for _ in range(II()):
    n, k = MII()
    c = n // k
    ans = []
    for i in range(k):
        ans.append(alpha[i] * c)
        # print(ans, c)
    ans.append('a' * (n % k))

    print(''.join(ans))


