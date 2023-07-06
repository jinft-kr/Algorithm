# N 크기 저장
N = int(input())
# 격자에 들어갈 정보 배열에 저장
data = [list(map(int, input().split())) for _ in range(N)]
# 가장자리에 0을 대입해야 함으로 N +2 크기의 [0]으로만 이루어진 2차원 리스트(m)를 만든다.
grid = [[0] * (N+2) for _ in range(N+2)]

# 가장자리를 제외하여 격자에 들어갈 정보를 새로운 리스트에 저장
for i in range(N):
    for j in range(N):
        if i<N+2 and j <N+2:
            grid[i+1][j+1] = data[i][j]

result = 0

# 상하좌우 비교(0 < x < N + 1, 0 < y < N + 1)
for x in range(N + 2):
    for y in range(N + 2):
        if 0 < x < N + 1 and 0 < y < N + 1:
            # 자기자신을 제외한 max_num
            max_num = max(grid[x][y - 1], grid[x][y + 1], grid[x - 1][y], grid[x + 1][y])
            # 자기 자신이 상하좌우 값의 최댓값보다 크다면
            if grid[x][y] > max_num:
                result += 1

print(result)