import sys

input = sys.stdin.readline

N = int(input().strip())

value = {}

for _ in range(N):
    key = int(input().strip())
    if key in value.keys():
        value[key] += 1
    else:
        value[key] = 1

for i in sorted(value):
    for _ in range(value[i]):
        print(i)