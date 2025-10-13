import sys

input = sys.stdin.readline

N = int(input().strip())
arr1 = list(map(int,input().split()))
M = int(input().strip())
arr2 = list(map(int,input().split()))

s = set(arr1)
answer = []

for i in range(M):
    answer.append(int(arr2[i] in s))

print((' ').join(map(str, answer)))