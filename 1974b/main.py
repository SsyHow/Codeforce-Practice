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

def main():
    for i in range(int(input())):
        n = int(input())
        s = input()
        t = sorted(set(s))
        pf = dict(zip(t, t[::-1]))
        print(''.join(pf[x] for x in s))


main()
