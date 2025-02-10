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

a = I()
s = I().split()

ans = 0
def f(k):
    ans = 0
    for i in k :
        if 'A' <= i <= 'Z':
            ans += 1
    return ans
for i in s:
    ans = max(ans, f(i))
print(ans)