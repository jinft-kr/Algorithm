# N 크기 저장
N = int(input())
# 격자에 들어갈 정보 리스트에 저장
grid=[list(map(int,input().split())) for _ in range(N)]
# 가장자리에 0을 둘러 쌓는 과정1 - 0번 행에 [0]으로 이루어진 n개의 리스트 추가
grid.insert(0,[0]*N)
# 가장자리에 0을 둘러 쌓는 과정2 - 맨 마지막 행에 [0]으로 이루어진 n개의 리스트 추가
grid.append([0]*N)

for x in grid:
    # 가장자리에 0을 둘러 쌓는 과정3 - 리스트 제일 앞에 0 추가
    x.insert(0,0)
    # 가장자리에 0을 둘러 쌓는 과정4 - 리스트 제일 뒤에 0 추가
    x.append(0)

# 상하좌우 비교를 위한 인덱스 좌표
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 봉우리 개수를 저장할 변수 선언
result = 0

# 상하좌우 비교(0 < x < N + 1, 0 < y < N + 1)
# 가장자리는 모두 0이기 때문에 첫번째 인덱스에서는 상하좌우를 비교하지 않아도 됨
for x in range(1, N + 1):
    for y in range(1, N + 1):
        # i+dx[k] : 행 / j+dy[k] : 열
        # 상하좌우를 비교했을 때 모든 경우가 자신이 큰 경우 봉우리 개수 + 1
        if all(grid[x][y] > grid[x+dx[k]][y+dy[k]] for k in range(4)):
            result += 1

print(result)