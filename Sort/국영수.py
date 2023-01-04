'''
[ 문제 ] : 국영수 (https://www.acmicpc.net/problem/10825)

[ 문제 풀이 ]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬

[ Concept ]
1. lamgda
- key 인자를 정하지 않은 기본적인 sort에선, 튜플 순서대로 우선순위 기본 할당
- key 인자에 함수를 넘겨주면 우선순위가 정해짐.
- 비교할 아이템이 요소가 복수 개일 경우, 튜플로 우선순위를 정해줄 수 있다.
- -를 붙이면, 현재와 반대차순으로 정렬된다.
'''
# 학생 정보 입력
students = [input().split() for _ in range(int(input()))]

students.sort(key=lambda score : (-int(score[1]), int(score[2]), -int(score[3]), score[0]))


for student in students:
    print(student[0])