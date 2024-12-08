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

    case1 = ''.join([s[0], s[1], s[2], s[3]])
    case2 = ''.join([s[0], s[1], s[2], s[b-1]])
    case3 = ''.join([s[0], s[1], s[b-2], s[b-1]])
    case4 = ''.join([s[0], s[b-3], s[b-2], s[b-1]])
    case5 = ''.join([s[b-4], s[b-3], s[b-2], s[b-1]])

    if case1 == '2020' or case2 == '2020' or case3 == '2020' or case4 == '2020' or case5 == '2020':
        print("YES")
    else:
        print("NO")
