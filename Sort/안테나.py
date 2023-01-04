'''
[ 문제 ] : 안테나 (https://www.acmicpc.net/problem/18310)

[ 문제 풀이 ]
1) 안테나는 집이 위치한 곳 중 한 곳에서만 설치할 수 있고, 모든 집 사이의 거리가 최소가 되어야 한다.
2) 따라서 모든 집의 위치 정보를 입력받고, 중앙값 출력

[ Concept ]

'''
n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data[(n-1)//2])