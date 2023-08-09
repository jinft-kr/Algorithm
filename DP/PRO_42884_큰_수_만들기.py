def solution(number, k):
    # 원본 변조를 피하기 위해 다른 변수에 카피해서 조작
    k_copy = k
    # 최종적으로 결과 값을 담아낼 스택
    queue = []

    for num in number:
        num = int(num)
        print("1. queue: ", queue, " / k : ", k_copy)
        # 스택에 숫자가 존재하고, 제거 횟수가 남아있고, 스택의 마지막 숫자가 현재 순회 숫자보다 작으면, 계속 스택을 pop하고 제거 횟수를 1 감소
        # queue에 큰 숫자 순서대로 정렬됨
        while len(queue) > 0 and k_copy > 0 and queue[-1] < num:
            queue.pop()
            k_copy -= 1
            print("2. queue: ", queue, " / k : ", k_copy)
        queue.append(num)
        print("3. queue: ", queue, " / k : ", k_copy)

    if k_copy != 0:
        queue = queue[:-k_copy]

    answer = "".join(map(str, queue))

    return answer
