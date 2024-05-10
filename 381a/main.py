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
b = LII()
ser = 0
dim = 0
l, r = 0, len(b)-1
flag = True
while l <= r:
    if flag:
        if b[l] > b[r]:
            ser += b[l]
            l += 1
        else:
            ser += b[r]
            r -= 1
    else:
        if b[l] > b[r]:
            dim += b[l]
            l += 1
        else:
            dim += b[r]
            r -= 1
    flag = not flag
print(ser, dim)

