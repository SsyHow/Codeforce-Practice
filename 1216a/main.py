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
s = I()
L = list(s)
x = k = y = 0
flag = 0
for i in range(a):
    if L[i] == 'a':
        x += 1
    else: y += 1

    if flag:
        if x > y:
            x -= 1
            y += 1
            L[i] = 'b'
            k += 1
        elif y > x:
            x += 1
            y -= 1
            L[i] = 'a'
            k += 1
    flag ^= 1

print(k)
print(''.join(L))

