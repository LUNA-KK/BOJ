import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한
input = sys.stdin.readline

# dfs 함수
def dfs(graph, v, visited):
    visited[v] = True # 노드 이름으로 방문 위치를 기록함
    for i in graph[v]:
        if not visited[i]: # visited[v]가 False 즉 아직 방문하지 않은 노드일 때
            dfs(graph, i, visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (n+1) # 탐색을 boolean으로 표시함
for i in range(1, n+1):
    if not visited[i]: # 방문하지 않은 곳
        dfs(graph, i, visited)
        count += 1 # dfs 한 번 끝날 때마다 count+1

print(count)
