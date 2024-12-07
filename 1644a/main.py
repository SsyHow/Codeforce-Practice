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
    s = I()
    stack = []
    for i in s:
        if i.islower():
            stack.append(i)
        else:
            # print(i.lower() not in stack)
            if i.lower() not in stack:
                print("NO")
                break
    else:
        print("YES")