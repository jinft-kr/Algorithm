'''
[ 문제 ] : 경쟁적 전 (https://www.acmicpc.net/problem/18405)

[ 예시 ]
1) 입력 조건
- 첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000)
- 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다.
- 각 행은 N개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다.
- 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다.
- 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다.
- N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)

2) 출력 조건
- S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다.
- 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

3) 입력 예시
3 3
1 0 2
0 0 0
3 0 0
2 3 2

4) 출력 예시
3

[ 문제 접근 방식 ]
- 차례대로 바이러스를 퍼트려야 하므로 큐를 사용한다.
- 바이러스의 종류, x, y값을 큐에 담는다.
- 바이러스 번호가 낮은 순서대로 큐를 정렬한다.
- 큐에 있는 모든 데이터가 bfs를 이용하여 상하좌우로 바이러스가 번식되도록 한다.
- 2번 과정을 각 초마다 실행하고 S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다.
- 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

[시간 복잡도]
'''

### [ 풀이 1 ] 바이러스 저장 구조(바이러스 종류, 위치 x, 위치 y)
from collections import deque

N, K = map(int, input().split())
graph = []
virus = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            virus.append(((graph[i][j], i, j)))

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(s, x, y):
    q = deque(virus)
    count = 0
    while q:
        if count == s:
            break
        for _ in range(len(q)):
            prev, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        q.append((graph[nx][ny], nx, ny))
        count += 1
    return graph[x - 1][y - 1]


virus.sort()
print(bfs(s, x, y))

### [ 풀이 2 ] 바이러스 저장 구조(바이러스 종료, 시간, 위치 x, 위치 y)
from collections import deque

n, k = map(int, input().split())

graph = []  # 전체 보드 정보를 담는 리스트
data = []  # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지의 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])