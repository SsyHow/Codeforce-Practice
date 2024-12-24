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
    x, y, m ,n = MII()
    mat = []
    for _ in range(x):
        mat.append(list(input()))
    if all(mat[i][j] == 'W' for j in range(y) for i in range(x)):
        print(-1)
    elif mat[m-1][n-1] == 'B':
        print(0)
    elif any(mat[j][n-1] == 'B' for j in range(x)) or any(mat[m-1][i] == 'B' for i in range(y)):
        print(1)
    else:
        print(2)