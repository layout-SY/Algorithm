import sys

input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    arr = list(map(int, input().strip().split()))
    for i in range(3):
        for j in range(9-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr[7])