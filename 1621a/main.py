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
    x, y = MII()
    if (x-1) // 2 + 1 < y:
        print(-1)
    else:
        mat = [['.' for _ in range(x)] for _ in range(x)]
        for i in range(y):
            mat[i*2][i*2] = 'R'
        for i in mat:
            print(''.join(i))