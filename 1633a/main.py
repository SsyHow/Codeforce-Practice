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
    if 1<= b < 10:
        print(7)

    elif b%7 == 0:
        print(b)

    elif 10 <= b < 100:
        for i in range(1,10):
            if (i*10 + b % 10) % 7 == 0:
                print(i*10 + b % 10)
                break
            elif (b//10 * 10  + i) % 7 == 0:
                print(b//10 * 10 + i)
                break

    else:
        for i in range(1, 10):
            if (i * 100 + b % 100) % 7 == 0:
                print(i * 100 + b % 100)
                break
            elif (b // 10 * 10 + i) % 7 == 0:
                print(b // 10 * 10  + i)
                break
            elif (b - b % 100 // 10 * 10 + i*10)% 7 == 0:
                print(b - b % 100 // 10 * 10 + i*10)
                break
