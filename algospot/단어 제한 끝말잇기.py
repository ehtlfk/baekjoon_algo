# 오일러 서킷  == 한줄 긋기, 시작점에서 다 거치고 시작점으로 돌아오거나, 끝점이 존재하기.

# 각 단어의 시작과 끝을 node로 지정
# 단방향이 맞나? 
# 한 번 쓴 단어는 사용 금지

# 오답이유 : dfs(0) 생각해보니 이게 마지막 단어면 의미가 없다. dfsAll을 잊지 말자
# dfsAll 방문하지 않았으면서 적어도 뒤에 한개는 있는 단어, => 는 당연히 안된다 컴포넌트가 여러개면 틀림
# 철자를 정점으로 **단어를 간선으로 활용**
import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

def dfs(x,y):
    for i in range(26):
        if adj_arr[y][i] != 0:
            adj_arr[y][i]-=1
            dfs(y,i)
    trail.append(graph[x][y])
sub = ord('a')
for _ in range(int(input())):
    N = int(input())
    words = [input().strip() for _ in range(N)]
    graph = [[0]*26 for _ in range(26)]
    adj_arr = [[0]*26 for _ in range(26)]
    edge = []
    trail =[]

    for i in range(len(words)):
        x = ord(words[i][0])-sub
        y = ord(words[i][-1])-sub
        graph[x][y] = words[i]
        adj_arr[x][y]+=1
    
             
    for i in range(26):
        for j in range(26):
            if adj_arr[i][j]:
                dfs(i,j)

    ans = list(reversed(trail[:-1]))
    if len(ans) == len(words):
        print( ' '.join(ans))
    else:
        print('IMPOSSIBLE')
