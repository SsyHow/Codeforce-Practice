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

a = I()

count = 0
for i in a:
    if i == '4' or i == '7':
        count += 1

for i in str(count):
    if i != '4' and i != '7':
        print('NO')
        break
else:
    print("YES")
