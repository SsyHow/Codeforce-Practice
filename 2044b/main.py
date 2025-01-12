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
    b = I()
    ans = []
    for i in b:
        if i == 'p':
            ans.append('q')
        elif i == 'q':
            ans.append('p')
        else:
            ans.append('w')
    print(''.join(ans[::-1]))