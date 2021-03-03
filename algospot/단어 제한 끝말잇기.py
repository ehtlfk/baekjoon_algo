# 오일러 서킷  == 한줄 긋기, 시작점에서 다 거치고 시작점으로 돌아오거나, 끝점이 존재하기.

# 각 단어의 시작과 끝을 node로 지정
# 단방향이 맞나? 
# 한 번 쓴 단어는 사용 금지

# 오답이유 : dfs(0) 생각해보니 이게 마지막 단어면 의미가 없다. dfsAll을 잊지 말자
# dfsAll 방문하지 않았으면서 적어도 뒤에 한개는 있는 단어, => 는 당연히 안된다 컴포넌트가 여러개면 틀림
# 철자를 정점으로 **단어를 간선으로 활용**
# dag나 dg 나 같고 간선이 다름. 아 순서가 상관없네 그러면...
# 간선을 이용한다 == degree
# list 26*26개  graph = [[] for _ in range(26)]*26 
import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

def dfs(x):
    print(x)
    for i in range(26):
        while adj_arr[x][i] > 0:
            adj_arr[x][i]-=1
            dfs(i)
    trail.append(x)

sub = ord('a')
for _ in range(int(input())):
    N = int(input())
    words = [input().strip() for _ in range(N)]
    graph = [[[] for _ in range(26)] for _ in range(26)] 
    adj_arr = [[0]*26 for _ in range(26)]
    trail =[]
    indegree = [0]*26
    outdegree = [0]*26
    for i in range(len(words)):
        x = ord(words[i][0])-sub
        y = ord(words[i][-1])-sub
        graph[x][y].append( words[i] )
        adj_arr[x][y]+=1
        indegree[y] +=1
        outdegree[x] +=1
    
             
    for i in range(26):
        if outdegree[i] >0:
            dfs(i)
    # ans = list(reversed(trail[:-1]))
    ans = list(reversed(trail))
    print(ans)
    # if len(ans) == len(words):
    for i in range(len(ans)-1):
        
        print(graph[ans[i]][ans[i+1]].pop())
    # print( ' '.join(ans))
    # else:
    #     print('IMPOSSIBLE')
