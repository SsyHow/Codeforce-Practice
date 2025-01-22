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

a = II()
for _ in range(a):
    m, n = MII()
    ma = [['0' for _ in range(n)] for _ in range(m)]
    ma[0][0] = ma[0][n-1] = ma[m-1][0] = ma[m-1][n-1] = '1'
    for j in range(1, n-1):
        if ma[0][j-1] == '0' and ma[0][j+1] == '0':
            ma[0][j] = '1'
        if ma[m-1][j-1] == '0' and ma[m-1][j+1] == '0':
            ma[m-1][j] = '1'
    for i in range(1, m-1):
        # print(i, ma[i-1][0], ma[i+1][0])
        if ma[i-1][0] == '0' and ma[i+1][0] == '0':
            ma[i][0] = '1'
        if ma[i-1][n-1] == '0' and ma[i+1][n-1] == '0':
            ma[i][n-1] = '1'


    for i in ma:
        print(''.join(i))