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

a, b = MII()
mat = []
for _ in range(a):
    mat.append(list(I()))
# print(mat)
r = c = 0
for i in range(a):
    if "S" not in mat[i]:
        r += 1
matt = [*zip(*mat)]
for i in range(b):
    if 'S' not in matt[i]:
        c += 1
print((r*b + c*a) - r*c)