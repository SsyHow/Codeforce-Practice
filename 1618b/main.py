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
    L = LI()
    ans = [L[0][0]]
    flag = True
    for i in range(b-3):
        # print(ans)
        if L[i][1] == L[i+1][0]:
            ans.append(L[i][1])
        else:
            flag = False
            ans.append(L[i][1])
            ans.append(L[i+1][0])
    ans.append(L[-1][1])

    if flag:
        ans.append(L[-1][1])
    print(''.join(ans))