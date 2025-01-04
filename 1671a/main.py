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
    s = '^' + I() + '$'
    prev = s[0]
    tmp = 1
    for i in s:
        if i == prev:
            tmp += 1
        else:
            if tmp < 2:
                print("NO")
                break
            prev = i
            tmp = 1
    else:
        print("YES")