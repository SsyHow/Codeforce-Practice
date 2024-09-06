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
L = LII()
cnte = 0
cnto = 0
laste = 0
lasto = 0
for i in range(a):
    if L[i] % 2 == 0:
        cnte += 1
        laste = i
    else:
        cnto += 1
        lasto = i

    if cnto and cnte and cnto > cnte:
        # print(cnto, cnte)
        print(laste+1)
        break
    elif cnto and cnte and cnte > cnto:
        # print(cnto, cnte)
        print(lasto+1)
        break
