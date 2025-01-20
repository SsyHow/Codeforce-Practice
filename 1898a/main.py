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
    b, c = MII()
    s = I()

    x = s.count('B')

    if x == c:
        print(0)
        continue
    if x > c:
        ans = 'A'
    else:
        ans = 'B'
    print(1)
    pos = cnt =  0
    for i in s:
        if ans != i:
            pos += 1
        cnt += 1

        if ans == "A" and x - pos == c:
            break
        elif x +pos == c:
            break
    print(cnt, ans)


