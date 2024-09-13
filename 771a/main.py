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
seat = []
flag = True
for i in range(a):
    b  = I()
    if flag and 'OO' in b:
        b = b.replace('OO', "++", 1)
        flag = False
    seat.append(b)

if flag:
    print("NO")
else:
    print("Yes")

    for i in seat:
        print(i)