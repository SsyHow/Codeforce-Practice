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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
for _ in range(a):
    b = II()
    c = I()

    prev = c[0]
    tmp = 1
    L = []

    for i in c[1:]:
        if i == prev:
            tmp += 1
        else:
            L.append(tmp)
            tmp = 1
            prev = i
    # if tmp > 1:
    L.append(tmp)
    ans = 0
    stack = -1
    for i in range(len(L)):
        # print(L[i], L[i] & 1)
        if L[i] & 1 == 1:
            if stack != -1:
                ans += i - stack
                stack = -1
            else:
                stack = i
        # print(i, stack)
    print(ans)