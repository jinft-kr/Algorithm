'''
[ 문제 ] : 실패율 (https://www.acmicpc.net/problem/18310)

[ 문제 풀이 ]
1) 각 스테이지별 실패율을 구한다.
2) 실패율을 기준으로 내림차순 정렬을 하며, 실패율이 같은 경우 오름차순으로 정렬한다.

[ Concept ]

'''
# N: 스테이지 개수, stages: 사용자가 현재 멈춰있는 스테이지의 번호


def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    # 정렬된 스테이지 번호 반환
    answer = [i[0] for i in answer]
    return answer