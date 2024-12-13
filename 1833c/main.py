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
    L = sorted(LII())

    flag = True
    if L[0] % 2 == 1:
        flag = False
    odd = 0
    for i in L:
        if flag == (i % 2 == 0):
            if not odd and i % 2 == 1:
                odd = i


        elif flag and i % 2 == 1:
            if not odd:
                print("NO")
                break
        elif not flag and i % 2 == 0:
            if not odd:
                print("NO")
                break
        # print(i % 2 == 1 , not odd)

    else:
        print("YES")


