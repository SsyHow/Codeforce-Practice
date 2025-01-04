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
    s = I()
    sums = sum([int(i) for i in s])
    s2 = s.count('2')
    s3 = s.count('3')

    modd = sums % 9
    if modd == 0:
        print("YES")
        continue
    flag = False
    for i in range(s2 + 1):
        for j in range(s3 + 1):
            tmp = modd + i * 2 + j * 6
            if tmp % 9 == 0:
                flag = True
                break
        if flag:
            break
    print("YES" if flag else "NO")


