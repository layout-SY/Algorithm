import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, [input().strip() for _ in range(n)]))

for i in sorted(arr):
    print(i)