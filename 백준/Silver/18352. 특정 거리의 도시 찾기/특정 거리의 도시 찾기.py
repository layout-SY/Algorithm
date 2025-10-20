import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M, K, X = map(int, input().strip().split())
distance = [INF] * (N+1) 
answer = []

arr = [[] for _ in range(N+1)]
for _ in range(M):
    n, m = map(int, input().strip().split())
    arr[n].append((m, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, i = heapq.heappop(q)
        if dist > distance[i]:
            continue
        for v, w in arr[i]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(X)

for i, num in enumerate(distance):
    if num == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    print('\n'.join(map(str, answer)))
