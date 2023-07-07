cache_hit = 1
cache_miss = 5

# list 이용
def solution(cacheSize, cities):
    answer = 0
    cache = []  # 담아줄 캐시리스트 변수
    if cacheSize == 0 : # 캐시 사이즈가 0일때
        return len(cities) * cache_miss
    else : 
        for city in cities:
            city = city.lower() # 문자열을 소문자로 변환한다.
            if city in cache: # 캐시에 city가 있을 경우
                cache.remove(city) # 캐시에 있는 기존 city 값 제거
                cache.append(city) # 캐시에 새로운 city 값 추가
                answer += cache_hit
            else: # 캐시에 city가 없을 경우
                answer += cache_miss
                if len(cache) == cacheSize: #캐시가 가득 차있을 경우
                    cache.pop(0) # 캐시에 있는 가장 오래된 city 값 제거
                cache.append(city) # 캐시에 새로운 city 값 추가
    return answer

import collections

# deque & maxlen 옵션 이용
def solution2(cacheSize, cities):
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += cache_hit
        else:
            cache.append(s)
            time += cache_miss
    return time
