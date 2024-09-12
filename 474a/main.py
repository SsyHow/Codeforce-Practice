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

b = -1 + 2 * (I() == 'L')
s = 'qwertyuiopasdfghjkl;zxcvbnm,./'
for i in I():
    print(s[s.index(i) + b], end='')
