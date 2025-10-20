import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().strip().split())
    arr[a].append((b, c))

start, end = map(int, input().strip().split())
distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, index = heapq.heappop(q)

        if dist > distance[index]:     
            continue

        for v, w in arr[index]:
            cost = w + dist
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(start)

sum = 0
for i, num in enumerate(distance):
    if start == i or end == i:
        sum += num

print(sum)