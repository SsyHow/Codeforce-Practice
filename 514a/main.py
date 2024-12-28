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

a = I()
ans = ''
for i in a:
    if (c:=int(i)) >= 5:
        ans += str(9-c)
    else:
        ans += i
print(ans) if ans[0] != '0' else print('9' + ans[1:])