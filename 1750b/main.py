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
    b = II()
    c = I()
    ones = 0
    zeros = 0
    tmp = 1
    prev = c[0]
    o = 0 if prev != '0' else 1
    z = 0 if prev != '1' else 1

    for i in c[1:]:
        if i == '0':
            o += 1
        else:
            z += 1
        if i != prev:
            if prev == '0':
                zeros = max(zeros, tmp)
                prev = '1'
            else:
                ones = max(ones, tmp)
                prev = '0'
            tmp = 1
        else:
            tmp += 1
        # print(o, z)
    if prev == '0':
        zeros = max(zeros, tmp)
    else:
        ones = max(ones, tmp)

    print(max(ones * ones, zeros * zeros, o * z))
