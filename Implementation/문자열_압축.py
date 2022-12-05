def solution(s):
    result = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s) + 1):
        str = ''
        count = 1
        tmp = s[:i]

        for j in range(i, len(s) + i, i):

            if tmp == s[j:i + j]:
                count += 1
            else:
                if count != 1:
                    str = str + str(count) + tmp
                else:
                    str = str + tmp

                tmp = s[j:j + i]
                count = 1

        result.append(len(str))

    return min(result)
print(solution(input()))