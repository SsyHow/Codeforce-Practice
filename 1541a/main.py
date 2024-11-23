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
    b = II()
    if b % 2 == 0:
        for i in range(1, b+1):
            if i % 2 == 0:
                print(i - 1, end =' ')
            else:
                print(i+1, end = ' ')
    else:
        print("3 1 2", end = ' ')
        for i in range(4, b+1):
            if i % 2 == 0:
                print(i + 1, end =' ')
            else:
                print(i - 1, end = ' ')
    print()