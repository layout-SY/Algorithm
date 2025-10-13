import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(list(x for x in input()) for _ in range(N))

visited = list(([0] * M) for _ in range(N))

answer = 0

def DFS(i, j, shape):
    if 0 > i or i >= N or 0 > j or j >= M or visited[i][j] or shape != arr[i][j]:
        return

    visited[i][j] = 1

    dx, dy = [1, 0] if shape=='-' else [0, 1]

    DFS(i+dy, j+dx, shape)

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            DFS(i, j, arr[i][j])
            answer += 1

print(answer)


