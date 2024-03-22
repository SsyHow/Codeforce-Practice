def I():
    return int(input())
def SI():
    return input()
a = I()
ans = 0
for i in range(a):
    b = SI()
    if '+' in b:
        ans += 1
    else:
        ans -= 1
print(ans)