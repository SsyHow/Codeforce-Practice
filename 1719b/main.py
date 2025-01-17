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
    b, c = MII()

    if c % 4 == 0:
        print("NO")
        continue

    print("YES")
    if c & 1 == 0:
        for i in range(1, b+1, 2):
            if (i + 1) % 4 == 0:
                print(i, i+1)
            else:
                print(i+1, i)
    else:
        for i in range(1, b+1, 2):
            print(i, i+1)
