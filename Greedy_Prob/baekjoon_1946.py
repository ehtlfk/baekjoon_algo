import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# 동석차 없음, N<=10^5, 서류, 면접 순 순위
# 선발할 수 없는 인원 수를 구하면 됨
# 그리디는 뒤에 것이 앞에 영향을 미칠 경우 !, 이걸 무시할 수 있나 없나를 평가

# 어떤 경우가 있나.. 5,7 4,8 3,6
T = int(input())
for _ in range(T):
    N = int(input())
    grade = [tuple(map(int,input().split())) for _ in range(N)]
    
    s_grade = sorted(grade, key=lambda x:x[0])

    cnt = 0
    x1,y1 = s_grade[0]
    for i in range(1,N):
        x,y = s_grade[i]
        if y > y1:
            cnt+=1
        else:
            y1 = y
    print(N-cnt) 

