import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

# 동석차 없음, N<=10^5, 서류, 면접 순 순위
# 선발할 수 없는 인원 수를 구하면 됨
# 그리디는 뒤에 것이 앞에 영향을 미칠 경우 !, 이걸 무시할 수 있나 없나를 평가
T = int(input())
for _ in range(T):
    N = int(input())
    grade = [tuple(map(int,input().split())) for _ in range(N)]
    

    s_grade = sorted(grade, reverse=True, key=lambda x:x[0])
    cnt = 0
    for i in range(N-1):
        _,y1 = s_grade[i]
        _,y2 = s_grade[i+1]
        if y1 > y2:
            cnt+=1

    print(N-cnt) 

