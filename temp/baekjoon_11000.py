import sys, os
BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline



N = int(input())
course = []
for _ in range(N):
    s,t = map(int,input().split())
    course.append((s,t))
s_course = sorted(course, key=lambda x:(x[0],x[1]))

cnt = 1
queue = [s_course[0][1]]
for i in range(1,N):
    if s_course[i-1][0] == s_course[i][0] and s_course[i-1][0]!=s_course[i-1][1]:
        cnt+=1
    elif queue[0] > s_course[i][0]:
        cnt+=1
    else:
        queue.pop(0)
        
    queue.append(s_course[i][1])
    
print(cnt)

    


