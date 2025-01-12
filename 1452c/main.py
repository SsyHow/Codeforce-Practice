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
    dic = {'(':0, '[':0}
    s = I()
    ans = 0
    for i in s:
        if i == '(' or i == '[':
            dic[i] += 1
        elif i == ')' and dic['('] > 0:
            ans += 1
            dic['('] -= 1
        elif i == ']' and dic['['] > 0:
            ans += 1
            dic['['] -= 1
    print(ans)



