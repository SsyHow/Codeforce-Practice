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

a, b, c = MII()

for i in range(1, 102):
    if i > a or i + 1 > b or i + 2 > c:
        print(i *3)
        break
