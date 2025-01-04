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

# a, b = MII()
# c = a %(b * 2)
# # print(b, c)
# print("YNEOS"[b > c::2])

a = II()
for _ in range(a):
    s = I()
    print(s)
    if s == 'Tomori':
        print('Haruhikage')

