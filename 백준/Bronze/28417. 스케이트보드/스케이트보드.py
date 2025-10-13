import sys

input = sys.stdin.readline

N = int(input().strip())

total = 0
for _ in range(N):
    temp = 0
    score = list(map(int, input().split()))
    head = score[:2]
    tail = sorted(score[2:], reverse=True)
    temp = max(head)
    temp = tail[0] + tail[1] + temp
    total = max(total, temp)

print(total) 