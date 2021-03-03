def solution(genres, plays):
    # 장르 재생 고유 번호
    answer = []
    c = dict()
    d = dict()
    for idx, g,p in zip(range(len(genres)),genres,plays):
        if d.get(g,0):
            c[g]+=p
            d[g].append((idx,p))
        else:
            c[g] = p
            d[g] =[(idx,p)]   
    play_cnt = sorted(d.keys(), reverse = True, key=lambda x: c[x]) # 이거 정렬 value로 해주는거임? lambda 키 두개? ,딕셔너리를 헷갈림
    
    for key in play_cnt:
        answer.extend( [v[0] for v in sorted(d[key], reverse = True, key=lambda x: (x[1],x[0])) ][:2])

        
    return answer


    # 인간적으로 너무 날먹이라 다른 언어로 풀어보자