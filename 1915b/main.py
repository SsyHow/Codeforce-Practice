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

def check(s):
    if '?' in s:
        if 'A' in s and 'B' in s:
            print('C')
        if 'C' in s and 'B' in s:
            print('A')
        if 'A' in s and 'C' in s:
            print('B')

a = II()
for i in range(a):
    for _ in range(3):
        s = I()
        check(s)


