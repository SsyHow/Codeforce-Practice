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

dic = {"purple" : "Power", "green": "Time",  "blue":"Space",  "orange" : "Soul", "red": "Reality", "yellow":"Mind"}
a = II()
k = set()

for _ in range(a):
    k.add(I())
print(6 - a)
for i in dic:
    if i not in k:
        print(dic[i])


