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
    b = II()
    mt = []
    loc = []
    for i in range(b):
        s = I()
        s = list(s)
        for j in range(b):
            if s[j] == '*':
                loc.append([i, j])
        mt.append(s)
    # print(loc, loc[0][1])
    if loc[0][1] != loc[1][1] and loc[0][0] != loc[1][0]:
        mt[loc[0][0]][loc[1][1]] = '*'
        mt[loc[1][0]][loc[0][1]] = '*'
    elif loc[0][1] == loc[1][1]:

        mt[loc[0][0]][(loc[1][1] + 1)%b] = '*'
        mt[loc[1][0]][(loc[0][1] + 1)%b] = '*'
    elif loc[0][0] == loc[1][0]:
        mt[(loc[0][0] + 1)%b][loc[0][1]] = '*'
        mt[(loc[1][0] + 1)%b][loc[1][1]] = '*'
    for i in mt:

        print(''.join(i))
