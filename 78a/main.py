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
vowel = {'a', 'e', 'i', 'o', 'u'}
def f(s):
    ans = 0
    for i in s:
        if i in vowel:
            ans += 1
    return ans

if f(I()) == 5 and f(I()) == 7 and f(I()) == 5:
    print("YES")
else:
    print("NO")
