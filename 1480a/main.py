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
    for i in range(len(b)):
        if i % 2 == 0:
            ans.append('a') if b[i] != 'a' else ans.append('b')
        else:
            ans.append('z') if b[i] != 'z' else ans.append('y')
    print(''.join(ans))