INF = int(1e9) # 초기 설정값 무한으로 초기화

# 노드의 개수 및 간선의 개수 입력
n, m = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한ㅇ느로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드의 X와 최종 목적지 노드 K 입력
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
# 각 라운드별로 중간 노드가 될 노드 번호를 for문 가장 바깥의 k로 삼는다.
# 내부 이중 for문에는 i, j를 통해 각 노드별 모든 거리를 살펴보면서
# k를 중간 노드로 삼을 때와 아닐 때의 값을 비교해 더 작은 값으로 업데이트한다.
for k in range(1, n+1):
    for a in range(1, n+1): # 최단 거리 배열인 dist 배열 구하기
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력 : 1번 노드에서 K에 들렸다가 X에 가는 최소거리
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
# 도달 할 수 있다면, 최단 거리를 출력
else:
    print(distance)
