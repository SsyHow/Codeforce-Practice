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
    c = LII()
    ans = [c[0]]
    if len(c) == 1:
        print(len(ans))
        print(' '.join([str(i) for i in ans]))
    else:
        prev = c[0]
        for i in c[1:]:
            if prev > i:
                ans.append(i)
            ans.append(i)
            prev = i
        print(len(ans))
        print(' '.join([str(i) for i in ans]))