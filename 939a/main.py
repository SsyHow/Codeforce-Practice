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
L = LII()
dic = {}
for idx, x in enumerate(L):
    dic[idx+1] = x

for i in dic:
    if i == dic[dic[dic[i]]]:
        print("YES")
        break
else:
    print("NO")