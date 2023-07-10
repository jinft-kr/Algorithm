# length = [int(input()) for _ in range(9)]
length = []
for i in range(9):
    length.append(int(input()))

# 일곱 난쟁이의 키를 오름차순으로 출력해야하기 때문에 정렬
length.sort()

# 일곱 난쟁이의 키 총합
sum_length = sum(length)

for i in range(len(length)):
    for j in range(i + 1, len(length)):
        # 일곱 난쟁이의 키가 100인 경우 일곱난쟁이 출력
        if sum_length - length[i] - length[j] == 100:
            for k in range(len(length)):
                if k == i or k == j:
                    pass
                else:
                    print(length[k])
            exit()