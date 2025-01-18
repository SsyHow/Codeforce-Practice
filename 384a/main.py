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
print(a*a //2 if a & 1 == 0 else a*a //2 + 1)
flag = True
for _ in range(a):

    if flag:
        print("C." * (a//2) + 'C' * (a%2))
    else:
        print(".C" * (a//2) + "." * (a%2))
    flag = not flag
