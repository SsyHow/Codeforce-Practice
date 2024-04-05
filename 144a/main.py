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
b = LII()

minv = min(b)
maxv = max(b)

maxindex = b.index(maxv)
minindex = len(b) - b[::-1].index(minv)-1
# print(maxindex, minindex)
if minindex < maxindex:
    print(maxindex + (len(b) - minindex - 1) - 1)
else:
    # print(1)
    print(maxindex + (len(b) - minindex - 1) )