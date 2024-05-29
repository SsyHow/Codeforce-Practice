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

for i in range(a):
    lenset = II()

    L = I()
    prev = L[0]
    seen = {prev}

    for i in L[1:]:
        if prev != i and i in seen:
            print("NO")
            break
        else:
            prev = i
            seen.add(i)
    else:
        print("YES")