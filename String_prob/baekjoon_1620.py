import sys
sys.stdin = open('String_prob/baekjoon_1620.txt')

# readline은 '\n'을 못 지운다 ^^, splite하면 없어지는데, 그냥 input 으로 받으면 있음
input = sys.stdin.readline
N,M = map(int, input().split())
pokedex = dict()
# 여기에서 먼저 선언하면 되는데
pokenum = dict()
for n in range(N):
    temp = input().replace('\n','')
    pokedex[temp] = n+1
    pokenum[n+1] = temp
# dict의 items는 tuple을 return하므로 unpacking 해주면된다.
# 특이하게 문자열 숫자를 key값으로 넣어주었는데, 알아서 int로 바뀐다.
for _ in range(M):
    temp = input().replace('\n','')
    if temp.isdigit():
        print(pokenum[int(temp)])
    else:
        print(pokedex[temp])


# 이걸 더줄여? 인풋 속도를 빨리 하니 통과는 하였는데 원래 문제의 의도가 과연 이것일까?

# 알고리즘 항목을 보니 '해쉬를 이용한 집합과 맵'과 '트리를 이용한 집합과 맵'이 나온다. 내가 활용한 방법은 해쉬를 이용한 방식이다.
# dict가 어떤 식으로 구현되어있는지를 알 필요가 있음