import sys
sys.stdin = open('String_prob/baekjoon_1620.txt')

N,M = map(int, input().split())

pokedex = dict()

for n in range(N):
    pokedex[input()] = n+1
# dict의 items는 tuple을 return하므로 unpacking 해주면된다.
# 특이하게 문자열 숫자를 key값으로 넣어주었는데, 알아서 int로 바뀐다.
pokenum = { val:key for key, val in pokedex.items()}

for _ in range(M):
    temp = input()
    if pokedex.get(temp):
        print(pokedex[temp])
    else:
        print(pokenum[int(temp)])