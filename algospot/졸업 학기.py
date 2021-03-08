import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
# 이 문제는 수가 많으면, BFS를 사용해서 풀어야 하지 않을까? 선수과목을 미리 수강해야 하므로

# 한 과목도 수강하지 않으면 휴학

# 열리는 학기가 제한인 과목

# 아니 이걸 어떻게 DP를 생각해, 매학기 마다 남은 최소 학기를 구한다.,
# 가장 좋은 방법은 완전 탐색, 조합탐색을 해야한다. 12C10, MAX 60가지, 제한시간이 3초인 이유가 있구나 

 # 이거 너무 별로인데, => 만약 cnt가 1로 같은데 둘중 하나밖에 못들을 경우, 못들은 과목이 나머지 과목의 선수 과목일 경우, 우선 순위는 선수 과목이 되는 과목 수 였다-> 알방법이 없나? 그래프? 수가 적은데 제한시간이 길다 -> 완전탐색
# index값을 return 해야함, [2,0,1,3]
for _ in range(int(input())):
    N, K, M, L = map(int, input().split())
    R = [0]*N   
    C = [0]*M
    for i in range(N):
        r = list(map(int,input().split()))
        if r[0]:
            for j in range(r[0]):
                R[i] += ((1<<N)-1 & (1 << r[j+1]))
    
    for i in range(M):
        c = list(map(int,input().split()))
        if c[0]:
            for j in range(c[0]):
                C[i] += ((1<<N)-1 & (1 << c[j+1]))

    current = 0
    cnt = 0
    course_cnt= course(C)
    for m in range(M):
        if K == 0:
            break
        temp = 0
        temp_cnt = L
        for i in order_course(C[m],course_cnt):
            # 선수과목이 0일 경우
            if temp_cnt == 0:
                break
            if not current & (1<<i):
                if R[i]:
                    if (R[i] & current) == R[i]:
                        temp += 1<<i
                        K-=1
                        temp_cnt -=1
                else:
                    temp += 1<<i
                    K-=1
                    temp_cnt-=1
        current|=temp
        if temp:
            cnt+=1
    if K:
        print('IMPOSSIBLE')
    else:
        print(cnt)
    
    