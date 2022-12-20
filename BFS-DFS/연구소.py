'''
[ 문제 ] : 연구소

[ 예시 ]
1) 입력 조건
- 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
- 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
- 빈 칸의 개수는 3개 이상이다.

2) 출력 조건
- 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

3) 입력 예시
4 4 2 1
1 2
1 3
2 3
2 4

4) 출력 예시
4

[ 문제 접근 방식 ]
- 벽을 꼭 3개를 세워야함으로 벽 3개를 세울 수 있는 모든 경우의 수를 구한다.
- 각 경우의 수 별로 벽이 세워졌을 때 바이러스를 퍼뜨린다.
- 각 경우의 수에서 바이러스가 퍼졌을 때 안전한 영역의 개수를 구한다.
- 각 경우의 수와 이전에 구한 안전한 영여의 개수를 비교하여 최대값을 구한다.

[시간 복잡도] O(N+M)
최대 전체 크기가 8*8 이므로
벽을 설치할 수 있는 모든 조합의 수는 최악의 경우 (바이러스가 하나도 존재 X)
64C3 이다.
100,000 보다 작은 수이므로, 모든 수를 고려해도 제한 시간 안에 문제를 해결 할 수 있다.
'''
# [ 풀이 1 ] DFS로 조합 구하기

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

result = 0

# 입력 받은 맵 정보 저장
for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 바이러스를 퍼뜨리는 함수
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_safezone():
    safezone = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safezone += 1
    return safezone

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        result = max(result, get_safezone())
        return
    # 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)

### [ 풀이 2 ] combinations 모듈로 조합 구하기
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

origin = deepcopy(data)

empty = []
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            empty.append((i, j))

walls = list(combinations(empty, 3))
result = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                score += 1
    return score


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                dfs(nx, ny)


for wall in walls:
    for wall_locate in wall:
        data[wall_locate[0]][wall_locate[1]] = 1
    for i in range(N):
        for j in range(M):
            if data[i][j] == 2:
                dfs(i, j)
    result = max(result, get_score())
    # 여기서 deepcopy 를 쓰지 않고 data=origin 으로 갱신시켰더니 data와 origin 이 메모리 주소가 복사되어 갱신이 제대로 되지 않았었음
    data = deepcopy(origin)

print(result)