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

matrix = [[] for i in range(5)]

for i in range(5):
    matrix[i] = LII()
    if sum(matrix[i]) == 1:
        for j in range(5):
            if matrix[i][j] == 1:
                x, y = i, j

print(abs(x-2) + abs(y - 2))