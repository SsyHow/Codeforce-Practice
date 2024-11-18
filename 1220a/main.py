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

b = I()
zero = b.count('z')
one = b.count('n')

for _ in range(one):
    print(1, end = ' ')
for _ in range(zero):
    print(0, end = ' ')
print()