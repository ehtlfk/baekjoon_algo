# lru는 가장 오랫동안 참조되지 않은 데이터를 버리는 것
# cache size가 없을 경우를 잘 처리 못함
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    d = dict()
    for ori_city in cities:
        city = ori_city.lower() # 대소문자 구분을 하지 않음
        if d.get(city,0):
            q.remove(city) # 어떤 식으로 구현되어있는지 모름
            answer+=1
        else:
            answer+=5
        if cacheSize:
            d[city] = 1
            q.append(city)
        if len(q) > cacheSize: # q에 추가를 했는데 cacheSize를 넘으면 제거
            d[q.popleft()] = 0            
            
    return answer