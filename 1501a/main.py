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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(int(input())):
	a,d=[],[0,]
	n=int(input())
	for j in range(n):
		x,b=map(int,input().split())
		a.append(x)
		d.append(b)
	t=list(map(int,input().split()))
	tt=0
	dp=0
	for j in range(n):
		tt=t[j]+dp+a[j]-d[j]
		dp=max(d[j+1],tt+(d[j+1]-a[j]+1)//2)
	print(tt)
