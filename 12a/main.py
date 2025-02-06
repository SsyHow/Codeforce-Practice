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

L =[]
for _ in range(3):
    L.append(list(I()))

if L[0][0] == L[2][2] and L[0][1] == L[2][1] and L[0][2] == L[2][0] and L[1][0] ==L[1][2]:
    print("YES")
else:
    print("NO")