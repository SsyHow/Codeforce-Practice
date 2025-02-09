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
s = I()
vowel = set(['a', 'e', 'i', 'o', 'u', 'y'])
L = []
flag = False
for i in s:
    if i not in vowel:
        L.append(i)
        flag = False
    elif i in vowel and flag:
        continue
    elif i in vowel and not flag:
        L.append(i)
        flag = True

print(''.join(L))