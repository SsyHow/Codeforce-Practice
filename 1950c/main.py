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
    b = I()
    if b[:2] == '00':
        print('12' + b[2:] + ' AM')
    elif int(b[:2]) >= 12:
        if b[:2] == '12':
            print(b + " PM")
        elif (int(b[:2]) - 12) < 10:
            s = '0' + str(int(b[:2]) - 12)
            print(s + b[2:] + ' PM')
        else:
            s = str(int(b[:2]) - 12)
            print(s + b[2:] + ' PM')
    else:
        print(b + ' AM')