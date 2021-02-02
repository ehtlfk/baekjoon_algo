import sys
sys.stdin = open('String_prob/baekjoon_1620.txt')

N,M = map(int, input().split())

pokedex = dict()
# 여기에서 먼저 선언하면 되는데
pokenum = dict()
for n in range(N):
    temp = input()
    pokedex[temp] = n+1
    pokenum[n+1] = temp
# dict의 items는 tuple을 return하므로 unpacking 해주면된다.
# 특이하게 문자열 숫자를 key값으로 넣어주었는데, 알아서 int로 바뀐다.

for _ in range(M):
    temp = input()
    if temp.isdigit():
        print(pokenum[int(temp)])
    else:
        print(pokedex[temp])