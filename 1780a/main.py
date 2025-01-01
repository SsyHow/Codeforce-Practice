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

a = II()
for _ in range(a):
    b = II()
    L = LII()
    even = []
    odd = []
    for i in range(b):
        if L[i] & 1 == 0:
            even.append(i)
        else:
            odd.append(i)

    if len(odd) >= 3:
        print("YES")
        print(odd[0]+1, odd[1]+1, odd[2]+1)
    elif len(odd) > 0 and len(even)> 1:
        print("YES")
        print(odd[0]+1, even[0]+1, even[1]+1)
    else:
        print("NO")