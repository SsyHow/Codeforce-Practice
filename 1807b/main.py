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
    od = 0
    odL = [i for i in L if i % 2]
    ev = sum(i for i in L if i % 2 == 0)
    for i in odL:
        od += i
        if od >= ev:
            print("NO")
            break
    else:
        print("YES")