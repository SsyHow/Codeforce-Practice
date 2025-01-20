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

def f(k):
    return k * (k-1) // 2

a = II()
for _ in range(a):
    b, c = MII()

    for i in range(b//2+2):
        # print(f(i) , f(b-i))
        if f(i) + f(b-i) == c:
            print("YES")
            print('1 ' * i + '-1 '* (b-i))
            break
    else:
        print("NO")