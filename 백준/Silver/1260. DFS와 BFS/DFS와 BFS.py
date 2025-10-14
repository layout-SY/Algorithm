import sys
from collections import deque

input = sys.stdin.readline

N, M, O = map(int, input().strip().split())

arr = [[] for _ in range(N+1)]
visitedDFS = [0] * (N+1)

for _ in range(M):
    n, m = map(int, input().strip().split())
    arr[n].append(m)
    arr[m].append(n)

for i in range(N+1):
    arr[i].sort()

def BFS(root):
    visited = [0] * (N+1)

    q = deque([root])
    visited[root] = 1

    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in arr[node]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

def DFS(root):
    print(root, end=' ')

    visitedDFS[root] = 1

    for i in arr[root]:
        if not visitedDFS[i]:
            visitedDFS[i] = 1
            DFS(i)

DFS(O)
print('')
BFS(O)
print('')



