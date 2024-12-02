import sys
input = sys.stdin.readline
from collections import deque


# 1)
# T = int(input())
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# # DFS/BFS 함수
# def DFS(r, c):

#     # 탐색(델타 탐색)
#     for d in range(4):
#     # 새로운 좌표를 찍어보고
#         nr, nc = r+dr[d], c+dc[d]

#     # 유효성 검사 후
#         if 0 <= nr < N and 0 <=nc < M and field[r][c] == 1 and (nr, nc) not in visited:
#             visited.add((r,c))
#     # 예정지에 넣기
#             DFS(nr, nc)

# for _ in range(T):
#     M, N, K = map(int, input())

#     # 빈 이차원리스트 만들기(N*M)
#     field = [[0] * M for _ in range(N)]

#     for _ in range(K):
#         c, r = map(int, input().split())
#         # 배추 심기
#         field[r][c] = 1

#     ########################################

#     # 초기 세팅(출발지, 예정지, 기록지)
#     visited = set()
#     cnt = 0

#     for r in range(N):
#         for c in range(M):
#             # 1이고, 방문한적 없다면?
#             if field[r, c] == 1 and (r,c) not in visited:
#                 visited.add((r,c))
#                 # BFS/DFS
#                 DFS(r, c)
#                 # +1
#                 cnt += 1
            
#     print(cnt)


# # 2)
# T = int(input())
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# for _ in range(T):
#     M, N, K = map(int, input().split())

#     cabbages = set()
#     for _ in range(K):
#         c, r = map(int, input().split())
#         cabbages.add((r,c))

#     while cabbages:
#         # 세팅(출발지, 예정지)
#         r, c = cabbages.pop()
#         queue = deque([(r,c)])

#         while queue:
#             # 방문
#             r, c = queue.popleft()

#             # 탐색
#             for d in range(4):
#                 nr, nc = r+dr[d], c+dc[d]
#                 if (nr, nc) in cabbages:
#                     cabbages.discard((nr, nc))
#                     queue.append((nr, nc))

#         cnt += 1

# # 3)
# from collections import deque

# T = int(input())
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# N, K = map(int, input().split())

# # 초기 세팅(출발지, 예정지, 기록지)
# queue = deque([(N, 0)])
# visited = set([N])

# # 예정지가 빌 때까지
# while queue:
#     # 방문
#     cur, cnt = queue.popleft()
#     # 해당 점이 K인지 검토
#     if cur == K:
#         break

#     # 탐색
#     # (X+1, X-1, 2*X)중에서
#     for nxt in [cur+1, cur-1, cur*2]:
#         # 방문한적 없다면?
#         if 0<= nxt < 140000 and nxt not in visited:
#             # 방문 체크하고
#             visited.add((nxt))
#             # 예정지에 넣기(nxt, cnt+1)
#             queue.append((nxt, cnt+1))

#     print(cnt)


# 4)
import sys
input = sys.stdin.readline

N = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
visited[0] = 1
ans = float("INF")

# 초기 세팅(출발지, 기록지, 예정지)
def DFS(cur, cost, depth):
    global ans
    # 방문
    if depth == N:
        if cost_matrix[cur][0]:
            cost += cost_matrix[cur][0]
            ans = min(ans, cost)
        return

    # 탐색(다음에 갈 곳을 찾아서)
    for nxt in range(N):
        if cost_matrix[cur][nxt] != 0 and not visited[nxt]:
            # 방문체크하고
            visited[nxt] = 1
            # 바로 방문
            DFS(nxt, cost+cost_matrix[cur][nxt], depth+1)
            # 방문체크 해제
            visited[nxt] = 0


DFS(0, 0, 1)
print(ans)