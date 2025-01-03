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
    n, m, v = MII()
    a = LII()

    sums = [0] * (n + 1)
    for i in range(n):
        sums[i+1] = sums[i] + a[i]


    def query(i, j):
        return sums[j] - sums[i]


    def compute_pfx():
        pfx = [0] * (n + 1)
        end = 0
        sum_val = 0
        for start in range(n):
            while end < n and sum_val < v:
                sum_val += a[end]
                end += 1
                pfx[end] = max(pfx[end], pfx[end - 1])
            if sum_val >= v:
                pfx[end] = 1 + pfx[start]
            sum_val -= a[start]
        for i in range(1, n + 1):
            pfx[i] = max(pfx[i], pfx[i - 1])
        return pfx


    pfx = compute_pfx()
    a.reverse()
    sfx = compute_pfx()
    a.reverse()
    sfx.reverse()

    if pfx[n] < m:
        print("-1")
        continue

    end = 0
    ans = 0
    for start in range(n):
        while end < n and pfx[start] + sfx[end + 1] >= m:
            end += 1
        if pfx[start] + sfx[end] >= m:
            ans = max(ans, query(start, end))

    print(ans)
