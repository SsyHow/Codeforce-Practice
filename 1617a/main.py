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

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
for _ in range(a):
    b = I()
    c = I()
    k = [0]  * 26
    for i in b:
        k[ord(i) - ord('a')] += 1
    # print(k)
    if c == 'abc' and k[1] > 0 and k[2] > 0 and k[0]> 0 :
        print(alpha[0] * k[0] + alpha[2] * k[2] + alpha[1] * k[1] + ''.join([alpha[i] * k[i] for i in range(3, 26)]))
    else:
        print(''.join([alpha[i] * k[i] for i in range(26)]))

