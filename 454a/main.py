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
k = a//2 + 1
for i in range(1, a + 1):
    if i <= k:
        print(''.join(['*'] * ((a - 2 * i + 1)//2) + ['D'] * (2 * i - 1) + ['*'] * ((a - 2 * i + 1)//2)))
    else:
        i = a - i +1
        print(''.join(['*'] * ((a - 2 * i + 1) // 2) + ['D'] * (2 * i - 1) + ['*'] * ((a - 2 * i + 1) // 2)))
