'''
[ 문제 ] 치킨 배달 (https://www.acmicpc.net/problem/15686)

1. 치킨집과 가정집의 좌표를 리스트에 저장
2. 치킨집 조합 구하기
3. 조합에서 가장 작은 수의 치킨거리 구하기

[ Tip ]
- DFS 탐색으로 조합을 구하는게 Combination 모듈을 사용하여 조합을 구하는것 보다 빠르다.
1) dfs : 288ms
2) combination : 424ms
'''

# [ 풀이 1 ] dfs 를 활용하여 조합 생성
from collections import deque

def distance(chicken):  # 거리를 계산하는 함수
    dist = 0
    for r1, c1 in home:
        dist += min([(abs(r1 - r2) + abs(c1 - c2)) for r2, c2 in chicken])
    return dist


def dfs(n, index):  # 조합을 만들어 치킨 거리의 최솟값을 찾는 함수 # n: 고른 치킨집 수 i: 고른 치킨집 번호
    global min_dist

    # 모든 치킨집을 골랐다면 치킨거리 계산
    if n == M:
        select_chicken = [chicken[i] for i in range(chickenCount) if visited[i]]
        min_dist = min(min_dist, distance(select_chicken))
        return

    # DFS 사용하여 조합 구하기
    for i in range(index, chickenCount):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n + 1, i + 1)
            visited[i] = 0


if __name__ == "__main__":

    N, M = map(int, input().split())  # 도시 크기, 치킨집 개수
    city = deque([])  # 도시
    chicken = deque([])  # 치킨집
    home = deque([])  # 집

    for r in range(N):
        temp = list(map(int, input().split()))
        city.append(temp)  # 도시의 각 행에 대한 정보 추가
        for c in range(N):
            if temp[c] == 2:  # 치킨집인 경우
                chicken.append((r, c))
            elif temp[c] == 1:  # 집인 경우
                home.append((r, c))

    if len(chicken) == M:  # 이미 M개이므로 치킨집을 폐업시킬 필요가 없음
        print(distance(chicken))
    else:  # M개씩 조합을 만들어 도시의 치킨 거리의 최솟값을 찾아야 함
        min_dist = N * 2 * len(home)  # 총 치킨거리 임의의 큰 값
        chickenCount = len(chicken)
        visited = [0] * chickenCount
        dfs(0, 0)
        print(min_dist)

# [ 풀이 2 ] combinations 모듈을 활용하여 조합 생성
from itertools import combinations

def solution():
    global answer
    for chicken in combinations(chicken_list, M):
        chicken_dist_total = 0
        for house in house_list:
            chicken_dist = N * 2 * len(house) # 임의의 큰수
            for i in range(M):
                chicken_dist = min(chicken_dist, abs(house[0] - chicken[i][0]) + abs(house[1] - chicken[i][1]))
            chicken_dist_total += chicken_dist
        answer = min(answer, chicken_dist_total)
    return

if __name__ == '__main__':
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    house_list = deque([])
    chicken_list = deque([])
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house_list.append((i, j))
            elif city[i][j] == 2:
                chicken_list.append((i, j))
    answer = int(1e9)
    solution()
    print(answer)