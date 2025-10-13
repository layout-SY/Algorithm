import sys

input = sys.stdin.readline

N = int(input().strip())

value = {}

for _ in range(N):
    v = int(input().strip())
    if v in value.keys():
        value[v] += 1
    else:
        value[v] = 1

for i in sorted(value):
    for _ in range(value[i]):
        print(i)