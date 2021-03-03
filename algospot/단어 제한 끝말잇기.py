# 오일러 서킷  == 한줄 긋기, 시작점에서 다 거치고 시작점으로 돌아오거나, 끝점이 존재하기.

# 각 단어의 시작과 끝을 node로 지정
# 단방향이 맞나? 
# 한 번 쓴 단어는 사용 금지

# 오답이유 : dfs(0) 생각해보니 이게 마지막 단어면 의미가 없다. dfsAll을 잊지 말자
# dfsAll 방문하지 않았으면서 적어도 뒤에 한개는 있는 단어
import sys, os

BASE_DIR = os.path.splitext(os.path.realpath(__file__))[0] +  '.txt'
sys.stdin = open(BASE_DIR)
input = sys.stdin.readline

def dfs(node):
    v [node] = 1
    for i in range(len(words)):
        if v[i] == 0 and adj_arr[node][i] == 1:
            adj_arr[node][i]-=1
            dfs(i)
    trail.append(node)
sub = ord('a')
for _ in range(int(input())):
    N = int(input())
    words = [input().strip() for _ in range(N)]
    edge = []
    adj_arr = [[0]*len(words) for _ in range(len(words))]
    
    trail =[]

    for i in range(len(words)):
        for j in range(len(words)):
            if words[i][0] == words[j][-1]:
                adj_arr[j][i] = 1
            if words[i][-1] == words[j][0]:
                adj_arr[i][j] = 1

    v =[0]*len(words)            
    for i in range(len(words)):
        for j in range(len(words)):
            if v[i] == 0 and adj_arr[i][j] == 1:
                dfs(i)
                break


    if len(trail) == len(words):
        print( ' '.join([ words[i] for i in reversed(trail)]))
    else:
        print('IMPOSSIBLE')
