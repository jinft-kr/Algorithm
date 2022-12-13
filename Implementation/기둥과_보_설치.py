'''
[ 문제 ] : 기둥과 보 설치 (https://programmers.co.kr/learn/courses/30/lessons/60061)
벽면의 크기 n, 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame이 매개변수로 주어질 때,
모든 명령어를 수행한 후 구조물의 상태를 return 하도록 solution 함수를 완성해주세요.

[ 조건 ]
- 설치 가능 조건
1) 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
2) 보는 한 쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

- 추가 조건
1) 만약 작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시됩니다.
2) 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
3) 바닥에 보를 설치하는 경우는 없습니다.

- 결과 출력 조건
1) return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고 있어야 합니다.
2) return 하는 배열의 원소는 [x, y, a] 형식입니다.
3) 기둥과 보는 교차점 좌표를 기준으로 오른쪽, 또는 위쪽 방향으로 설치되어 있음을 나타냅니다.
4) return 하는 배열은 x 좌표 기준으로 오름차순 정렬, x,y 좌표가 같을 경우 y 좌표를 기준으로 오름차순 정렬
5) x, y 좌표가 모두 같은 경우 기둥이 보보다 앞면에 오면 됩니다.

[ 입출력 예시 ]
n
5
build_frame
[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
result
[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

[ 문제 접근 방법 ]
작업 순서대로 기둥 혹은 보를 설치/제거한 후 설치된 모든 기둥과 보들이 주어진 조건에 맞게 설치되어 있는지 확인한다.
1. 기둥 설치가 가능한 경우:
    1) 맨 밑에 있는 경우
    2) 설치 아래 지점에 기둥이 있는 경우
    3) 설치 왼쪽 지점에 보가 있는 경우
    4) 설치 지점에 보가 있는 경우
    -> 모든 조건을 만족하지 않으면 설치 불가능
2. 보 설치가 가능한경우 :
    1) 설치 아래 지점에 기둥이 있는 경우
    2) 설치 아래 오른쪽 지점에 기둥이 있는 경우
    3) 양 옆에 보가 있는 경우
    -> 모든 조건을 만족하지 않으면 설치 불가능
설치/제거가 불가능 한 경우는 작업을 수행하지 않는다.

[ Tip ]
- 중복을 허용하지 않는 구조일 경우 list 보단 set 을 사용하는 것이 속도가 빠르다.
- 또한 중복을 허용하지 않으며 데이터의 자료순서(혹은 정렬된상태)가 따로 필요하지 않다면 set을 사용하는 것이 속도가 빠르다.
- 따라서 set은 특정값이 이미 있는지 여부를 확인할 때 매우 효과적이다.
    - list 의 경우: O(n) # x in arr
    - set 의 경우 : O(1) # hash table 자료구조를 사용하기 때문에 빠른 탐색이 가능
'''
# [ 풀이 1 ] list 사용
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def isOk(result):
    for x, y, a, b in result:
        if a == 0 : # 설치된 것이 '기둥'인 경우
            # 조건 1) '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1 ,y, 1] in result or [x, y, 1]  in result or [x, y -1, 0] in result:
                continue
            return False
        if a == 1 : # 설치된 것이 '보'인 경우
            # 조건 2) '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [ x, y - 1, 0 ] in result or [ x + 1, y - 1, 0] in result or ([ x-1, y, 1] in result and [x+1, y, 1] in result) : # 조건 2
                continue
            return False
    return True

def solution(n, build_frame):
    result = [] # 리턴 형식 [x, y, a]
    for frame in build_frame: # 작업물 개수를 하나씩 확인 # 작업(frame)의 개수는 최대 1,000개 임으로 완전 탐색 가능
        x, y, stuff, operate = frame
        if operate == 1: # 설치하려는 경우
            # 일단 설치
            result.append(x, y, stuff) # 일단 설치를 해본 뒤에
            if not isOk(result): # 가능한 구조물인지 확인
                result.remove(x, y, stuff) # 가능한 구조물이 아니라면 다시 제거
        else : # 삭제하려는 경우
            result.remove(x, y, stuff) # 일단 삭제를 해본 뒤에
            if not isOk(result): # 가능한 구조물인지 확인
                result.append(x, y, stuff) # 가능한 구조물이 아니라면 다시 설치
    return sorted(result) # return 하는 배열을 X 좌표 기준으로 오름차순 정렬, x,y좌표 같을 경우 y 좌표를 기준으로 오름차순


# [ 풀이 2 ] set 사용
def impossible(result):
    for x, y, a in result:
        if a == 0:  # 기둥일 때
            if y != 0 and (x, y - 1, 0) not in result and \
                    (x - 1, y, 1) not in result and (x, y, 1) not in result:
                return True
        else:  # 보일 때
            if (x, y - 1, 0) not in result and (x + 1, y - 1, 0) not in result and \
                    not ((x - 1, y, 1) in result and (x + 1, y, 1) in result):
                return True
    return False


def solution(n, build_frame):
    result = set()

    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build:  # 추가일 때
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result:  # 삭제할 때
            result.remove(item)
            if impossible(result):
                result.add(item)
    answer = map(list, result)

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))