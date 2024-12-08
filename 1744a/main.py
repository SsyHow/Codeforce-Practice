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
    L = LII()
    s = I()
    dic = {}
    for i in range(b):
        if L[i] in dic:
            if dic[L[i]] != s[i]:
                print("NO")
                break
        else:
            dic[L[i]] = s[i]
    else:
        print("YES")