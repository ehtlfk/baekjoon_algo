import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
# 이 문제는 수가 많으면, BFS를 사용해서 풀어야 하지 않을까? 선수과목을 미리 수강해야 하므로

# 한 과목도 수강하지 않으면 휴학

# 열리는 학기가 제한인 과목
def course(arr):
    count =[0]*N
    for a in arr:
        for i in range(N): # 과목수만큼
            if 1 << i & a:
                count[i]+=1
    
    return count
def order_course(num,arr): # 이거 너무 별로인데
    course_list = []
    for i in range(N):
        if num & (1<<i):
            course_list.append(i)
    
    return sorted(course_list,key= lambda x:arr[x])
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
        for i in order_course(C[m],course_cnt)[:L]:
            # 선수과목이 0일 경우
            if not current & (1<<i):
                if R[i]:
                    if (R[i] & current) == R[i]:
                        temp += 1<<i
                        K-=1
                else:
                    temp += 1<<i
                    K-=1
        current|=temp
        if temp:
            cnt+=1
    if K:
        print('IMPOSSIBLE')
    else:
        print(cnt)
    
    