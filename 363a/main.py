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

def solve(k):
    k = int(k)
    ans = []
    if k <= 4:
        ans.append('O-|')
    else:
        k -= 5
        ans.append('-O|')

    ans.append('O' * k+'-' +'O' * (4 - k))
    print(''.join(ans))
a = I()
for i in a[::-1]:
    solve(i)
    # print('O-|OO-OO')
