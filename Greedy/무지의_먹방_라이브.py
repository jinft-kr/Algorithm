'''

'''
food_times = list(map(int, input().split()))
k = int(input())

def solution(food_times, k):
    result = 0
    index = 0

    # 음식을 모두 먹는 시간보다 k가 크면 -1 반환
    if k >= sum(food_times):
        result = -1
        return result

    while True:
        if k == 0:
            break
        # 더 섭취해야할 음식이 없다면 -1 반환
        if food_times.count(0) == len(food_times):
            result = -1
            break;
        # 현재 그릇에 섭취할 음식이 없으면 다음 음식 먹기
        if food_times[index] == 0:
            index = (index + 1) % len(food_times)
            continue
        else:
            food_times[index] = food_times[index] - 1
            index = (index + 1) % len(food_times)
            k -= 1

    while True:
        if result == -1:
            break
        if food_times[index] == 0:
            index = (index + 1) % len(str(index))
            continue
        else:
            result = index + 1
            break

    return result

def solution2(food_times, k):
    index_of_list = 0
    food_index_list = list(range(len(food_times)))

    if k >= sum(food_times):
        return -1
    while True:
        if k == 0:
            break

        if food_times[index_of_list] == 0:
            food_times.pop(index_of_list)
            food_index_list.pop(index_of_list)
            index_of_list = index_of_list % len(food_index_list)
            continue
        else:
            food_times[index_of_list] -= 1
            index_of_list = (index_of_list + 1) % len(food_index_list)
            k -= 1
    return food_index_list[index_of_list] + 1
print(solution2(food_times, k))
