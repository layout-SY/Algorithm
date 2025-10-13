import sys

input = sys.stdin.readline

N = int(input().strip())

arr = list(map(int, input().strip().split()))

arr.sort()

answer = 0

for i in range(N):
    start = 0
    end = N - 1
    while start < end:
        if arr[i] == (arr[start] + arr[end]):
            if (start != i) and (end != i):
                answer += 1
                break
            elif(start == i):
                start += 1
            elif(end == i):
                end -= 1
        elif (arr[start] + arr[end]) < arr[i]:
            start += 1
        else:
            end -= 1


print(answer)