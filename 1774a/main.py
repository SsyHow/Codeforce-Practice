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
    s = I()
    prev = 1 if s[0] == '1' else 0
    ans = []
    for i in s[1:]:
        if i == '1':

            if prev:
                ans.append('-')
            else:
                ans.append('+')
            prev ^= 1

        else:
            ans.append('+')
    print(''.join(ans))
