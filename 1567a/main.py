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
dic = {"L" : "L", "U" : "D", "D": "U", "R": "R"}
for _ in range(a):
    b = II()
    s = I()
    for i in range(b):
        print(dic[s[i]], end = '')
    print()
