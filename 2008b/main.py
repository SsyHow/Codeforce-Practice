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
    s = I()
    c = int(b ** 0.5)
    if c ** 2 != b:
        print("NO")
        continue
    # print(1)
    cs = '1' * c + ('1' + '0' * (c-2) + '1') * (c-2) + '1' * c
    # print(cs)
    # print(s)
    if cs == s:
        print("YES")
    else:
        print("NO")