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
    s = list(I())
    tmp = ['0'] * b
    for j in range(min(b, c)):
        for i in range(b):
            if s[i] == '1':
                tmp[i] = '1'
            # if 0 < i < b -1:
            #     print(s)
            #     print(j, ((s[i+1] == '1' , s[i - 1] == '0') , (s[i+1] == '0' , s[i - 1] == '1')))
            elif 0 < i < b -1 and s[i] == '0' and ((s[i+1] == '1' and s[i - 1] == '0') or (s[i+1] == '0' and s[i - 1] == '1')):
                tmp[i] = '1'
            elif i == 0 and s[i+1] == '1' and s[i] == '0':
                tmp[i] = '1'
            elif i == b - 1 and s[i] == '0' and s[i-1] == '1':
                tmp[i] = '1'
        # print(s, tmp)
        s = tmp.copy()
    print(*s, sep='')

