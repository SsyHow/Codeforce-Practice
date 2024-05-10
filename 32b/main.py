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

l = 0
r = 1
ans =''
while r <= len(a):
    if a[l] == '.':
        ans+='0'
        l+= 1
        r+= 1
    elif a[l:r+1] == '-.':
        ans+='1'
        l+= 2
        r+= 2
    elif a[l:r+1] == '--':
        ans+= '2'
        l+=2
        r+= 2
print(ans)
