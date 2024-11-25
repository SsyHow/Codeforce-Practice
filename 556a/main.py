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
stack = []
for i in I():
    if stack and i != stack[-1]:
        stack.pop()
    else:
        stack.append(i)
# print(stack)
print(len(stack))