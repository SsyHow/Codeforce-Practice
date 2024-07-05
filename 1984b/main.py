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
    b = I()
    if b[0] != '1':
        print("NO")
        continue
    if b[-1] == "9":
        print("NO")
        continue
    j = 1
    while j < len(b)-1:
        if b[j] == "0":
            print("NO")
            break
        j += 1
    else:
        print("YES")


