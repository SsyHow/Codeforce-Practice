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

a, b = MII()
s = I()

g = s.index('G')
t = s.index('T')
k = abs(g-t)

if k % b != 0:
    print("NO")
elif any(s[i] == '#' for i in range(min(g, t), max(g,t), b)):
    print("NO")
else:
    print("YES")