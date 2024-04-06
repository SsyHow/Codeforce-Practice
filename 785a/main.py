import sys
_input = input
def input():
    return sys.stdin.readline()
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
ans = 0
for i in range(a):
    ip = I().strip()
    if ip == 'Tetrahedron':
        ans += 4
    if ip == 'Cube':
        ans += 6
    if ip == 'Octahedron':
        ans += 8
    if ip == 'Dodecahedron':
        ans += 12
    if ip == 'Icosahedron':
        ans += 20
print(ans)